# Generated by Django 4.0.6 on 2022-08-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_about_social_imageabout'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
