# Generated by Django 5.1.7 on 2025-03-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practical_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='seller_con',
            field=models.CharField(default='0598921999', max_length=40),
        ),
    ]
