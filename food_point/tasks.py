from celery import shared_task

from food_point.models import Check
from services.convertor_html_to_pdf import check_to_pdf


@shared_task
def generate_pdf(instance_id):
    instance = Check.objects.get(id=instance_id)
    check_to_pdf(instance)
    instance.status = "rendered"
    instance.save()
