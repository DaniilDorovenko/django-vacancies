# Generated by Django 3.1 on 2020-12-04 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0010_auto_20201203_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancyapplication',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.vacancy'),
        ),
    ]
