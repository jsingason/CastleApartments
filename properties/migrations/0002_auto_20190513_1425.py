# Generated by Django 2.2.1 on 2019-05-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertiesaddress',
            name='houseNumber',
            field=models.IntegerField(),
        ),
    ]
