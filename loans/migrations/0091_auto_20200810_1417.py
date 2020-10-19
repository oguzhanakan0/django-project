# Generated by Django 3.0.7 on 2020-08-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0090_auto_20200810_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loantype',
            name='critical_principals',
        ),
        migrations.AddField(
            model_name='principal',
            name='loan_types',
            field=models.ManyToManyField(related_name='principals', to='loans.LoanType'),
        ),
    ]
