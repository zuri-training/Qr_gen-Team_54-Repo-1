# Generated by Django 4.0.6 on 2022-08-03 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0003_rename_qr_code_website_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='file',
        ),
    ]
