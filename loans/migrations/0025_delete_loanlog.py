# Generated by Django 3.0.7 on 2020-06-25 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0024_loanlog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoanLog',
        ),
    ]