# Generated by Django 4.2 on 2025-04-17 10:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('domain_no', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
