# Generated by Django 3.2.9 on 2021-11-30 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_id', models.TextField()),
                ('password', models.TextField()),
                ('total_amount', models.IntegerField()),
                ('name', models.TextField()),
                ('father_name', models.TextField()),
                ('village_ward', models.TextField()),
                ('post_office', models.TextField()),
                ('city', models.TextField()),
                ('district', models.TextField()),
                ('state', models.TextField()),
                ('pin', models.IntegerField()),
                ('due_cleared', models.BooleanField(default=False)),
                ('landmark', models.TextField()),
                ('phone_number', models.TextField()),
                ('aadhaar_number', models.IntegerField(max_length=12)),
                ('pan_number', models.IntegerField(max_length=10)),
                ('aadhaar_image', models.ImageField(upload_to='aadhaar_images')),
                ('pan_image', models.ImageField(upload_to='pan_images')),
                ('status', models.TextField(blank=True, default='pending')),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dealer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.dealer')),
            ],
        ),
    ]
