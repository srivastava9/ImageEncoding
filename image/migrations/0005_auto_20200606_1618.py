# Generated by Django 3.0.7 on 2020-06-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_remove_imagemodel_encoded_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
    ]
