# Generated by Django 4.1.7 on 2023-03-15 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_books_options_alter_books_co_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='data_cadastro',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
