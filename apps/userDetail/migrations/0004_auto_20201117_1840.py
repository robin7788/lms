# Generated by Django 3.1.3 on 2020-11-17 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
        ('userDetail', '0003_auto_20201117_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebookdetail',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Book.book'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issuebookdetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userDetail.userdetail'),
        ),
    ]