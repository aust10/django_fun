# Generated by Django 3.0.3 on 2020-04-09 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0003_auto_20200409_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitter',
            name='my_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
