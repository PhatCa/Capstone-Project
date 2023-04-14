# Generated by Django 4.2 on 2023-04-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ingredient', models.TextField()),
                ('instructions', models.TextField()),
                ('picture', models.CharField(max_length=255)),
            ],
        ),
    ]