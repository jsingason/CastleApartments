# Generated by Django 2.2.1 on 2019-05-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_auto_20190511_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
    ]
