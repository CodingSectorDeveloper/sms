# Generated by Django 3.2.9 on 2021-12-02 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_emi'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_id', models.TextField()),
                ('amount', models.IntegerField(default=0)),
                ('dealer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.dealer')),
            ],
        ),
    ]