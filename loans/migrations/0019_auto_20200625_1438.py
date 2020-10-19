# Generated by Django 3.0.7 on 2020-06-25 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loans', '0018_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='upd_program',
            field=models.ForeignKey(db_column='_program', default='not_specified', on_delete=django.db.models.deletion.PROTECT, to='loans.Program', to_field='program'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='upd_time',
            field=models.DateTimeField(auto_now_add=True, db_column='_upd_time', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='upd_user',
            field=models.ForeignKey(db_column='_user', default='admin', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, to_field='username'),
            preserve_default=False,
        ),
    ]
