import os.path, os
import subprocess
from dataclasses import dataclass

from django.template.loader import render_to_string
from django.core.files import File

from topfood import settings


@dataclass
class CheckToPDF:
    type: str
    order: dict


def check_to_pdf(check):
    check_pdf = CheckToPDF(check.type, check.order)
    cmd = ["wkhtmltopdf", "--quiet", "-", "-"]
    html = render_to_string("check_template.html", {"check": check_pdf})
    p = subprocess.run(cmd, input=html.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        raise ValueError(p.stderr.decode())
    filename = f'{check_pdf.order["order"]}_{check_pdf.type}.pdf'
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    with open(file_path, "wb") as f:
        f.write(p.stdout)
    with open(file_path, "rb") as f:
        check.pdf_file.save(filename, File(f))

# def check_to_pdf(check):
#     check_pdf = CheckToPDF(check.type, check.order)
#     docker_cmd = ["docker", "run", "--rm", "-i", "docker-wkhtmltopdf-arm", "wkhtmltopdf", "-", "-"]
#     html = render_to_string("check_template.html", {"check": check_pdf})
#     p = subprocess.run(docker_cmd, input=html.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     if p.returncode != 0:
#         raise ValueError(p.stderr.decode())
#     filename = f'{check_pdf.order["order"]}_{check_pdf.type}.pdf'
#     file_path = os.path.join(settings.MEDIA_ROOT, filename)
#     with open(file_path, "wb") as f:
#         f.write(p.stdout)
#     with open(file_path, "rb") as f:
#         check.pdf_file.save(filename, File(f))
