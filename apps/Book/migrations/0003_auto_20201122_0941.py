# Generated by Django 3.1.3 on 2020-11-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20201122_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_number',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
