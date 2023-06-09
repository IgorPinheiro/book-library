# Generated by Django 4.1.7 on 2023-03-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_books_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='co_autor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='tempo_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
