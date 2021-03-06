# Generated by Django 3.0.3 on 2020-04-02 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itmes', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='published date')),
                ('comp_date', models.DateTimeField(blank=True, null=True, verbose_name='compleated date')),
                ('is_comp', models.BooleanField(default=False)),
            ],
        ),
    ]
