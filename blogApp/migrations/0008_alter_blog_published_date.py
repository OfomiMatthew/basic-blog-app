# Generated by Django 4.2.3 on 2024-04-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0007_alter_blog_content_alter_blog_published_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
    ]
