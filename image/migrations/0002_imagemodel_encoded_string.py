# Generated by Django 3.0.7 on 2020-06-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='encoded_string',
            field=models.CharField(default='', max_length=1000),
        ),
    ]