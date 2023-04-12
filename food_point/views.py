import zipfile

from django.http import FileResponse, HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from food_point.models import Printer, Check
from food_point.serializers import PrinterSerializer, CheckSerializer
from food_point.tasks import generate_pdf


class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class CheckViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Check.objects.all().select_related("printer_id")
    serializer_class = CheckSerializer

    @action(detail=False, methods=["post"])
    def create_check(self, request):
        point_id = request.query_params["point_id"]
        printers = Printer.objects.filter(point_id=point_id)
        if Check.objects.filter(order=request.data).exists():
            return Response(f'Order {request.data["order"]} has already exists')
        if printers:
            for printer in printers:
                instance = Check.objects.create(
                    printer_id=printer,
                    type=printer.check_type,
                    order=request.data
                )
                instance_id = instance.pk
                generate_pdf.delay(instance_id)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(request.data)

    @action(detail=False, methods=["get"])
    def print_check(self, request):
        printer_id = request.query_params["printer_id"]
        rendered_checks = Check.objects.filter(printer_id=printer_id, status="rendered")
        files = [check.pdf_file for check in rendered_checks]
        response = HttpResponse(content_type="topfood/zip")
        response["Content-Disposition"] = 'attachment; filename="rendered_checks.zip"'
        with zipfile.ZipFile(response, "w") as zip_file:
            for file in files:
                zip_file.write(file.path, arcname=file.name)
        for check in rendered_checks:
            check.status = "printed"
            check.save()
        return response
