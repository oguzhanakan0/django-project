# Generated by Django 3.0.7 on 2020-06-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0042_auto_20200626_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loandetaillog',
            name='upd_time',
        ),
        migrations.AlterField(
            model_name='loanlog',
            name='upd_time',
            field=models.DateTimeField(db_column='_upd_time'),
        ),
    ]
