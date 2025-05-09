# Generated by Django 5.1.7 on 2025-03-16 11:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertisement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_requests', to='advertisement.advertisement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
