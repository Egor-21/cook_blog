# Generated by Django 4.0.6 on 2022-08-01 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cool_time',
            new_name='cook_time',
        ),
    ]
