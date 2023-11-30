# Generated by Django 4.2.5 on 2023-11-30 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0009_alter_autor_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='idade',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Idade'),
        ),
    ]
