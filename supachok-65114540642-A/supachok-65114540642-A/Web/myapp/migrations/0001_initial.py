# Generated by Django 5.1.1 on 2025-03-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
    ]
