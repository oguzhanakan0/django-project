# Generated by Django 3.0.7 on 2020-07-06 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0075_auto_20200706_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='logo_path',
            new_name='logo',
        ),
    ]