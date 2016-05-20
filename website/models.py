from django.db import models
from django.utils import timezone
from PIL import Image

class Categorias(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)

    def __str__(self):
        return self.nome

class CategoriasMacro(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)

    def __str__(self):
        return self.nome

class UnidadesMedida(models.Model):
    descricao = models.CharField(max_length=20, null=True,unique=True)
    categorias = models.ManyToManyField(CategoriasMacro)

    def __str__(self):
        return self.descricao

class Ingredientes(models.Model):
    nome = models.CharField(max_length=20,null=True)
    quantidade = models.FloatField(null=True)
    unidadeMedida = models.ManyToManyField(UnidadesMedida)

    def __str__(self):
        return self.nome

class Receitas(models.Model):
    autor = models.ForeignKey('auth.User', related_name='usuario')
    nome = models.CharField(max_length=20,unique=True)
    categoria=models.ForeignKey(
        Categorias,
        on_delete=models.CASCADE,
        null=True
        )
    dataCriacao = models.DateTimeField(
            default=timezone.now)
    ingredientes=models.ManyToManyField(Ingredientes)
    modoPreparo = models.TextField()
    tempoPreparo = models.TimeField()
    rendimento = models.PositiveIntegerField(null=True)
    grauDificuldade = models.PositiveIntegerField()
    avaliacao = models.PositiveIntegerField(null=True,default=0)
    imagem = models.ImageField(upload_to='fotos',null=True)

    def __str__(self):
        return self.nome
