# Generated by Django 3.2.9 on 2021-12-02 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_emi_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EMI',
        ),
    ]