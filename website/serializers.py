from rest_framework import serializers
from .models import Receitas, Ingredientes, CategoriasMacro, Categorias, ReceitasCategoria


class CategoriasMacroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasMacro
        fields = ('id', 'nome')

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ('id', 'nome')

class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = ('id', 'nome','quantidade','unidade_de_medida')

class ReceitasSerializer(serializers.ModelSerializer):
    categorias = CategoriasSerializer(many=True)
    ingredientes = IngredientesSerializer(many=True)

    class Meta:
        model = Receitas
        fields = ('id','nome','categorias','ingredientes','modo_de_preparo', 'tempo_de_preparo','rendimento','grau_de_dificuldade','imagem')

class ReceitasCategoriaSerializer(serializers.ModelSerializer):
    categorias = CategoriasSerializer(many=True)
    receitas =  ReceitasSerializer(many=True)
    macro = CategoriasMacroSerializer()

    class Meta:
        model = ReceitasCategoria
        fields = ('id','nome','categorias', 'receitas', 'macro')
