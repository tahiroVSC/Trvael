# Generated by Django 5.0.1 on 2024-01-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название тура')),
                ('description', models.CharField(max_length=500, verbose_name='Описание тура')),
                ('date', models.DateTimeField(verbose_name='Дата тура')),
                ('price', models.SmallIntegerField(verbose_name='Цена тура')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
    ]