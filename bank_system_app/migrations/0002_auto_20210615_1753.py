# Generated by Django 3.2.4 on 2021-06-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_system_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer_history',
            name='receiver',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='transfer_history',
            name='sender',
            field=models.CharField(max_length=50),
        ),
    ]
