# Generated by Django 3.0.7 on 2020-08-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0081_auto_20200802_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
    ]