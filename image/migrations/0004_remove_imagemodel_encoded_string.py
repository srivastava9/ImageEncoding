# Generated by Django 3.0.7 on 2020-06-06 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20200605_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='encoded_string',
        ),
    ]
