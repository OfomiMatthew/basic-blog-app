# Generated by Django 4.2.3 on 2024-03-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]