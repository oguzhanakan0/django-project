# Generated by Django 3.0.7 on 2020-06-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0037_auto_20200625_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanlog',
            name='loan_id',
            field=models.CharField(max_length=36),
        ),
    ]
