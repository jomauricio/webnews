from django.db import models

# Create your models here.

class Autor(models.Model):
    
    nome = models.CharField("Nome", max_length=200)
    data_nascimento = models.DateField("Data de Nascimento", default="1980-01-01")
    email = models.EmailField("Email")
    idade = models.PositiveSmallIntegerField("Idade")
    avatar = models.ImageField("Foto", upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return self.nome + " " + self.email
    
    class Meta:
        verbose_name = "Escritor"
        verbose_name_plural = "Escritores"
        permissions  = [
            ("pode_publicar", "Pode publicar uma noticia"),
        ]


class Noticia(models.Model):

    CATEGORIAS = [
        ("Urgente", "Urgente"),
        ("Esportes", "Esportes"),
        ("Política", "Política")
    ]

    titulo = models.CharField("Titulo", max_length=200)
    conteudo = models.TextField("Conteúdo")
    data_pub = models.DateField("Data de publicação")
    tags = models.CharField("Categoria", max_length=100, choices=CATEGORIAS)
    autor = models.ForeignKey(Autor, verbose_name="Autor", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"