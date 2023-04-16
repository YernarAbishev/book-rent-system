# Generated by Django 2.1.7 on 2023-04-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20230411_0918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Мекен-жай', 'verbose_name_plural': 'Мекен-жайлар'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Кітап', 'verbose_name_plural': 'Кітаптар'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Тапсырыс беруші', 'verbose_name_plural': 'Тапсырыс берушілер'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Төлем', 'verbose_name_plural': 'Төлемдер'},
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Кітап атауы'),
        ),
    ]
