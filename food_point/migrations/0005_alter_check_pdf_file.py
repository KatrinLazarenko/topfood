# Generated by Django 4.1.7 on 2023-04-12 15:54

from django.db import migrations, models
import food_point.models


class Migration(migrations.Migration):

    dependencies = [
        ('food_point', '0004_alter_check_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='pdf_file',
            field=models.FileField(upload_to=food_point.models.pdf_path),
        ),
    ]
