# Generated by Django 3.1.6 on 2021-02-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]