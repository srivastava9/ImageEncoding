# Generated by Django 3.0.7 on 2020-06-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0006_remove_imagemodel_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
