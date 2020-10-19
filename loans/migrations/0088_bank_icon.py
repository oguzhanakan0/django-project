# Generated by Django 3.0.7 on 2020-08-10 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('loans', '0087_loanmatrixtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]