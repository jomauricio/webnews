# Generated by Django 4.2.5 on 2023-11-14 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0005_alter_autor_avatar_alter_autor_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticia.autor', verbose_name='Autor'),
        ),
    ]