# Generated by Django 4.1.7 on 2023-03-28 16:32

from django.db import migrations, models
import django.db.models.deletion
import food_point.models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="Printer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("api_key", models.CharField(max_length=255, unique=True)),
                ("check_type", models.CharField(choices=[("kitchen", "kitchen"), ("client", "client")], max_length=10)),
                ("point_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Check",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("type", models.CharField(choices=[("kitchen", "kitchen"), ("client", "client")], max_length=10)),
                ("order", jsonfield.fields.JSONField(default=dict)),
                ("status", models.CharField(choices=[("new", "new"), ("rendered", "rendered"), ("printed", "printed")], max_length=10)),
                ("pdf_file", models.FileField(upload_to=food_point.models.pdf_path)),
                ("printer_id", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="food_point.printer")),
            ],
        ),
    ]