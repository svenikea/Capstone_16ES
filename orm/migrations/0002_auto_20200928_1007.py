# Generated by Django 3.1.1 on 2020-09-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='brand',
            field=models.ManyToManyField(related_name='shoes_brand', to='orm.shoes_brand'),
        ),
    ]
