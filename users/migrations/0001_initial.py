# Generated by Django 4.2.1 on 2023-05-12 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hotels.validators
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=100, validators=[users.validators.check_password])),
                ('username', models.CharField(max_length=255, validators=[users.validators.check_username])),
                ('phone', models.CharField(max_length=20, unique=True, validators=[hotels.validators.validate_phone_number])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('point', models.IntegerField(blank=True, default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('admin_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
