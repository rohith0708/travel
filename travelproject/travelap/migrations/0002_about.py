# Generated by Django 4.1.5 on 2023-02-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('imaage', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
