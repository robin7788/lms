# Generated by Django 3.1.3 on 2020-11-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDetail', '0008_auto_20201121_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuebookdetail',
            name='fine_note',
            field=models.TextField(blank=True),
        ),
    ]
