# Generated by Django 3.0.7 on 2020-06-22 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('bank', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('installment_type', models.CharField(max_length=100)),
                ('min_tenure', models.PositiveIntegerField()),
                ('max_tenure', models.PositiveIntegerField()),
                ('base_interest', models.FloatField()),
                ('insurance_type', models.CharField(max_length=100)),
                ('redirect_url', models.URLField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
