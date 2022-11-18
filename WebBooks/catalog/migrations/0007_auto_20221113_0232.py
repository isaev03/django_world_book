# Generated by Django 3.2.7 on 2022-11-12 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(help_text='Введите название книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='Название книги'),
        ),
    ]
