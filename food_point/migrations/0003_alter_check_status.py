# Generated by Django 4.1.7 on 2023-04-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food_point", "0002_alter_check_pdf_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="check",
            name="status",
            field=models.CharField(choices=[("new", "new"), ("rendered", "rendered"), ("printed", "printed")], default="new", max_length=10),
        ),
    ]
