# Generated by Django 3.1.7 on 2021-04-02 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20210402_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='date',
        ),
    ]