from django.db import models
from django.utils import timezone
from PIL import Image


class CategoriasMacro(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)

    def __str__(self):
        return self.nome


class Categorias(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)
    categoria_macro = models.ForeignKey(CategoriasMacro)

    def __str__(self):
        return self.nome

class Ingredientes(models.Model):
    nome = models.CharField(max_length=20,null=True)
    quantidade = models.FloatField(null=True)
    unidade_de_medida = models.CharField(max_length=15,null=True)

    def __str__(self):
        return '%s %s %s' % (self.nome, self.quantidade, self.unidade_de_medida)

    class Meta:
        unique_together = ["nome", "quantidade", "unidade_de_medida"]

class Receitas(models.Model):
    nome = models.CharField(max_length=50,unique=True)
    categorias=models.ManyToManyField(Categorias)
    data_de_criacao = models.DateTimeField(default=timezone.now)
    ingredientes=models.ManyToManyField(Ingredientes)
    modo_de_preparo = models.TextField()
    tempo_de_preparo = models.CharField(max_length=30,unique=True)
    rendimento = models.PositiveIntegerField(null=True)
    grau_de_dificuldade = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='fotos',null=True)

    def __str__(self):
        return self.nome

class ReceitasCategoria(models.Model):
    nome = models.CharField(max_length=50,unique=True)
    categorias = models.ManyToManyField(Categorias)
    receitas = models.ManyToManyField(Receitas)
    macro = models.ManyToManyField(CategoriasMacro)

    def __str__(self):
        return self.nome
