# Generated by Django 4.1.3 on 2023-01-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Familia', '0003_alter_family_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='dni',
            field=models.IntegerField(),
        ),
    ]
