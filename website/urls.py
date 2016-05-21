from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^macro/$',views.TodasAsCategoriasMacro.as_view()),
    url(r'^categorias/$',views.TodasAsCategorias.as_view()),
    url(r'^macro/categorias/(?P<pk>[0-9]+)/$',views.CategoriasEmCategoriasMacro.as_view()),
    url(r'^categoria/(?P<pk>[0-9]+)/$',views.ReceitasEmCategoria.as_view()),
    url(r'^receitas/$',views.TodasAsReceitas.as_view()),
    url(r'^receita/(?P<pk>[0-9]+)/$',views.DetalheReceita.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns = format_suffix_patterns(urlpatterns)
