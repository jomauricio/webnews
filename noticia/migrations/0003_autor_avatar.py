# Generated by Django 4.2.5 on 2023-10-03 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_autor_data_nascimento_autor_email_autor_idade'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
