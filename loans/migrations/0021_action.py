# Generated by Django 3.0.7 on 2020-06-25 12:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0020_auto_20200625_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('action', models.CharField(default='INSERT', max_length=40, unique=True)),
            ],
        ),
    ]
