# Generated by Django 3.0.3 on 2020-04-02 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitem',
            old_name='itmes',
            new_name='items',
        ),
    ]