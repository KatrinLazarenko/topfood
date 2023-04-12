from django.contrib import admin

from food_point.models import Printer, Check


class CheckAdmin(admin.ModelAdmin):
    list_display = ('printer_id', 'type', 'order', 'status', 'pdf_file')
    list_filter = ('printer_id', 'type', 'status')


admin.site.register(Printer)
admin.site.register(Check, CheckAdmin)
