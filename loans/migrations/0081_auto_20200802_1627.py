# Generated by Django 3.0.7 on 2020-08-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0080_auto_20200802_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loansummary',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]