# Generated by Django 2.2.1 on 2019-05-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=999)),
                ('image', models.CharField(blank=True, max_length=999)),
            ],
        ),
    ]