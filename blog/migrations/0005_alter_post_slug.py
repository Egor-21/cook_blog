# Generated by Django 4.0.6 on 2022-08-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_recipe_directions_alter_recipe_ingretions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]
