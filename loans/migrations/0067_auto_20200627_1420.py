# Generated by Django 3.0.7 on 2020-06-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0066_loanrequest_tenure'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='allocation_cost',
            field=models.PositiveIntegerField(default=25),
        ),
        migrations.AddField(
            model_name='loanlog',
            name='allocation_cost',
            field=models.PositiveIntegerField(default=25),
        ),
    ]
