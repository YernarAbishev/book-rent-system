# Generated by Django 2.1.7 on 2023-04-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230409_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(null=True, upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
