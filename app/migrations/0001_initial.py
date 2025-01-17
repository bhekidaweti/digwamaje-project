# Generated by Django 5.1.4 on 2025-01-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_service', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
