# Generated by Django 4.1.3 on 2022-12-28 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Familia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='dni',
            field=models.IntegerField(),
        ),
    ]
