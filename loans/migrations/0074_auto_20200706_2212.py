# Generated by Django 3.0.7 on 2020-07-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0073_loansummary_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='logo_path',
            field=models.ImageField(upload_to='images/bank_logo/'),
        ),
    ]