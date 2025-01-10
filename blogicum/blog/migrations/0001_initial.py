# Generated by Django 3.2.16 on 2025-01-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
