from django.shortcuts import render

def receitas_list(request):
    return render(request, 'website/receitas.html', {})

def index(request):
    return render(request, 'website/theme/index.html', {})
