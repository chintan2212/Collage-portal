# Generated by Django 3.1.5 on 2021-02-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('submitted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Courses', models.CharField(max_length=100)),
                ('Professor', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.CharField(max_length=100)),
                ('professor_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=20)),
            ],
        ),
    ]
