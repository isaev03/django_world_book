# Generated by Django 3.2.7 on 2022-11-12 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20221113_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите автора для книги', to='catalog.Author', verbose_name='Автор книги'),
        ),
    ]
