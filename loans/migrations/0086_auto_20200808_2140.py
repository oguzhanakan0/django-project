# Generated by Django 3.0.7 on 2020-08-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0085_auto_20200808_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanmatrix',
            name='min_interest',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
