# Generated by Django 3.1.3 on 2020-11-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDetail', '0006_auto_20201118_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuebookdetail',
            name='fine',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
