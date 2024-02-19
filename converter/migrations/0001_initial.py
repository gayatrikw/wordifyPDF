# Generated by Django 4.0.8 on 2024-01-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConvertedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('converted_file', models.FileField(upload_to='converted/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]