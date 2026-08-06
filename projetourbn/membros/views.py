# membros/views.py
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MembrosForm
from .models import Membros


# Página inicial (Home)
def home(request):
    return render(request, 'home.html')

def base(request, template_name='base.html'):  # Com valor padrão
    return render(request, template_name)

# Página de serviços
def services(request):
    # Dados dos serviços
    services_data = [
        {
            'id': 1,
            'name': 'Lavagem Completa',
            'description': 'Lavagem externa e interna completa',
            'price': '150,00',
            'duration': '2 horas',
            'icon': '💧',
            'features': ['Lavagem externa', 'Aspiração interna', 'Limpeza de vidros'],
            'featured': True,
        },
        {
            'id': 2,
            'name': 'Polimento',
            'description': 'Polimento profissional com máquina',
            'price': '250,00',
            'duration': '3 horas',
            'icon': '✨',
            'features': ['Polimento de pintura', 'Remoção de riscos', 'Cera protetora'],
            'featured': False,
        },
        {
            'id': 3,
            'name': 'Vitrificação',
            'description': 'Proteção cerâmica de longa duração',
            'price': '500,00',
            'duration': '6 horas',
            'icon': '🛡️',
            'features': ['Vitrificação 9H', 'Proteção UV', 'Fácil limpeza'],
            'featured': False,
        },
    ]
    return render(request, 'precos.html', {'services': services_data})

# Página de preços (mesmo conteúdo da services)
def prices(request):
    return services(request)

# Página sobre
def about(request):
    return render(request, 'about.html')

def header(request):
    return header(request, ' includes/header.html')

# Página de contato
def contact(request):
    return render(request, 'contact.html')

# SUAS VIEWS EXISTENTES...
def listar_membros(request):
    lista = Membros.objects.all().order_by('firstname')
    return render(request, 'membros/listar_membros.html', {"membros": lista})

def criar_membro(request):
    if request.method == "POST":
        form = MembrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_membros')
    else:
        form = MembrosForm()
    return render(request, 'membros/criar_membro.html', {"form": form})

def editar_membro(request, id):
    membro = get_object_or_404(Membros, id=id)
    if request.method == "POST":
        form = MembrosForm(request.POST, instance=membro)
        if form.is_valid():
            form.save()
            return redirect('listar_membros')
    else:
        form = MembrosForm(instance=membro)
    return render(request, 'membros/editar_membro.html', {"form": form, "membro": membro})

def deletar_membro(request, id):
    membro = get_object_or_404(Membros, id=id)
    if request.method == "POST":
        membro.delete()
        return redirect('listar_membros')
    return render(request, 'membros/confirmar_delecao.html', {"membro": membro})