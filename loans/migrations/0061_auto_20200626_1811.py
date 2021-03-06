# Generated by Django 3.0.7 on 2020-06-26 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0060_auto_20200626_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='tenure',
            field=models.ForeignKey(db_column='tenure', default=12, on_delete=django.db.models.deletion.PROTECT, to='loans.Tenure', to_field='tenure'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanlog',
            name='tenure',
            field=models.ForeignKey(db_column='tenure', default=12, on_delete=django.db.models.deletion.PROTECT, to='loans.Tenure', to_field='tenure'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='tenure',
            field=models.ForeignKey(db_column='tenure', default=12, on_delete=django.db.models.deletion.PROTECT, to='loans.Tenure', to_field='tenure'),
            preserve_default=False,
        ),
    ]
