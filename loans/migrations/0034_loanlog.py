# Generated by Django 3.0.7 on 2020-06-25 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0033_delete_loanlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanLog',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('loans.loan',),
        ),
    ]
