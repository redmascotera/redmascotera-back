# Generated by Django 5.0b1 on 2024-02-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example_field', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExampleUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example_field', models.CharField(max_length=255)),
            ],
        ),
    ]