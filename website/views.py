from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .serializers import CategoriasMacroSerializer, CategoriasSerializer, ReceitasSerializer, ReceitasCategoriaSerializer
from .models import CategoriasMacro, Categorias, Receitas, ReceitasCategoria
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate

class TodasAsCategoriasMacro(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CategoriasMacro.objects.all()
    serializer_class = CategoriasMacroSerializer

class TodasAsCategorias(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


class TodasAsReceitas(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializer


class DetalheReceita(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializer

class CategoriasEmCategoriasMacro(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CategoriasSerializer

    def get_queryset(self):
        macro = self.kwargs['pk']
        return Categorias.objects.filter(categoria_macro=macro).order_by('nome')

class ReceitasEmCategoria(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReceitasSerializer

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Receitas.objects.filter(categorias__id=categoria).order_by('nome')

class ReceitasEmCategoriaMacro(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReceitasCategoriaSerializer

    def get_queryset(self):
        macro = self.kwargs['pk']
        return ReceitasCategoria.objects.filter(macro__id=macro).order_by('nome')
