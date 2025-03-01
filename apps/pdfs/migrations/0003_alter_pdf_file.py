# Generated by Django 4.0.6 on 2022-08-03 12:42

import apps.common.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfs', '0002_alter_pdf_qr_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='file',
            field=models.FileField(upload_to='', validators=[apps.common.custom_validators.validate_pdf_file_type]),
        ),
    ]
