# Generated by Django 3.1.1 on 2020-09-19 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'verbose_name': 'List', 'verbose_name_plural': 'Lists'},
        ),
    ]
