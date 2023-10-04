from django.db import models

# Create your models here.

class Autor(models.Model):
    
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(default="1980-01-01")
    email = models.EmailField()
    idade = models.PositiveSmallIntegerField()
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return self.nome