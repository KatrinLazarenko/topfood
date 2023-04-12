import jsonfield
import os
from django.db import models

check_type_choice = (
    ("kitchen", "kitchen"),
    ("client", "client"),
)

check_status = (
    ("new", "new"),
    ("rendered", "rendered"),
    ("printed", "printed"),
)


def pdf_path(instance, filename):
    return os.path.join("media/pdf", filename)


class Printer(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255, unique=True)
    check_type = models.CharField(max_length=10, choices=check_type_choice)
    point_id = models.IntegerField()

    def __str__(self):
        return f"{self.point_id} {self.check_type}"


class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=check_type_choice)
    order = models.JSONField()
    status = models.CharField(max_length=10, choices=check_status, default="new")
    pdf_file = models.FileField(upload_to=pdf_path, blank=True, null=True)

    def __str__(self):
        return self.pdf_file.name
