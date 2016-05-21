from django.contrib import admin
from .models import Receitas
from .models import Categorias
from .models import CategoriasMacro
from .models import Ingredientes
from .models import Medidas

admin.site.register(Receitas)
admin.site.register(Categorias)
admin.site.register(CategoriasMacro)
admin.site.register(Ingredientes)
admin.site.register(Medidas)
