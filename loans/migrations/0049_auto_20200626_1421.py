# Generated by Django 3.0.7 on 2020-06-26 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0048_auto_20200626_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linklog',
            old_name='loan_link_id',
            new_name='link_id',
        ),
    ]
