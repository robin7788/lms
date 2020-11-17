# Generated by Django 3.1.3 on 2020-11-17 15:42

import apps.userDetail.current_user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Book', '0001_initial'),
        ('userDetail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueBookDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(auto_now=True)),
                ('return_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Book.book')),
                ('created_by', models.ForeignKey(blank=True, default=apps.userDetail.current_user.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userDetail.userdetail')),
            ],
        ),
    ]
