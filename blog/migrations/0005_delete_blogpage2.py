# Generated by Django 3.0.7 on 2020-07-06 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('blog', '0004_blogpage2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPage2',
        ),
    ]
