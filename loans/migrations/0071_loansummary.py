# Generated by Django 3.0.7 on 2020-07-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0070_bank_logo_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=40)),
                ('bank_logo_path', models.CharField(max_length=100)),
                ('loan_name', models.CharField(max_length=100)),
                ('min_principal', models.PositiveIntegerField()),
                ('max_principal', models.PositiveIntegerField()),
                ('min_tenure', models.PositiveIntegerField()),
                ('max_tenure', models.PositiveIntegerField()),
                ('interest', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
    ]
