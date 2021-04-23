# Generated by Django 3.2 on 2021-04-20 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210419_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Livro', models.CharField(max_length=50, verbose_name='Livro')),
                ('Autor', models.CharField(max_length=50, verbose_name='Autor')),
                ('Editora', models.CharField(max_length=30, verbose_name='Editora')),
                ('Preco', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade em Estoque')),
            ],
        ),
        migrations.DeleteModel(
            name='Livros',
        ),
    ]
