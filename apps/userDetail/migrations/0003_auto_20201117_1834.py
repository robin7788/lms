# Generated by Django 3.1.3 on 2020-11-17 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userDetail', '0002_issuebookdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuebookdetail',
            old_name='return_status',
            new_name='status',
        ),
    ]
