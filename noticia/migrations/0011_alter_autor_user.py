# Generated by Django 4.2.5 on 2023-11-30 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticia', '0010_alter_autor_data_nascimento_alter_autor_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='autor', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
