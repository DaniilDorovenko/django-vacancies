# Generated by Django 3.1 on 2020-12-04 12:59

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0016_auto_20201204_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
