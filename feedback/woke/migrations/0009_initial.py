# Generated by Django 4.1.7 on 2023-02-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('woke', '0008_delete_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dec', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
