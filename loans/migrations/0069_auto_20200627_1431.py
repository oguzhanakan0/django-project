# Generated by Django 3.0.7 on 2020-06-27 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0068_auto_20200627_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='allocation_fee',
        ),
        migrations.RemoveField(
            model_name='loanlog',
            name='allocation_fee',
        ),
    ]