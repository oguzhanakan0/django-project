# Generated by Django 3.0.7 on 2020-06-26 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0056_auto_20200626_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenure',
            name='loan_type',
            field=models.ForeignKey(db_column='loan_type', default='GPL', on_delete=django.db.models.deletion.PROTECT, to='loans.LoanType', to_field='loan_type'),
            preserve_default=False,
        ),
    ]
