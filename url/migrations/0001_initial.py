# Generated by Django 4.0.6 on 2022-07-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_original', models.URLField(unique=True)),
                ('url_curta', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
