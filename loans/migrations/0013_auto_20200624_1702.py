# Generated by Django 3.0.7 on 2020-06-24 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0012_auto_20200624_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='principal',
            name='principal',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.RemoveField(
            model_name='loan',
            name='bank_id',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loan_type_id',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='principal_id',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='tenure_id',
        ),
        migrations.AddField(
            model_name='loan',
            name='bank_name',
            field=models.ForeignKey(db_column='bank_name', default='ING Bank', on_delete=django.db.models.deletion.CASCADE, to='loans.Bank', to_field='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_type',
            field=models.ForeignKey(db_column='loan_type', default='GPL', on_delete=django.db.models.deletion.CASCADE, to='loans.LoanType', to_field='loan_type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='principal',
            field=models.ForeignKey(db_column='principal', default=50000, on_delete=django.db.models.deletion.CASCADE, to='loans.Principal', to_field='principal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='tenure',
            field=models.ForeignKey(db_column='tenure', default=12, on_delete=django.db.models.deletion.CASCADE, to='loans.Tenure', to_field='tenure'),
            preserve_default=False,
        ),
    ]
