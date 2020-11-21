# Generated by Django 3.1.3 on 2020-11-21 10:31

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDetail', '0007_issuebookdetail_fine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebookdetail',
            name='fine',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
    ]
