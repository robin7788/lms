# Generated by Django 3.1.3 on 2020-11-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0006_remove_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/book'),
        ),
    ]