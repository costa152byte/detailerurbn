from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from .forms import Membrosform
from .models import Membros


def Listar_membros(request):
    lista = Membros.objects.all().order_by ('firstname') 
    return render(request, "meuprimeiro.html", {"Membros": lista})

def criar_membro(request):
    if request.method == "POST": 
        form = Membrosform(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('listar_membros')
    else:
        form = Membrosform()
    return render(request, "criar_membro.hmtl", {"form": form})

def editar_membro(request, id):
    membro = get_list_or_404(Membros, id=id)

    if request.method == "POSt":
       form = Membrosform(request.POST, instance=membro)

    if form.is_valid():
        form.save()

        return redirect('listar_membros')
    else:
     
        form = Membrosform(instance=membro)
    return render(request), "editar_membro.html", {"form": form, "membro": membro}

def deletar_membro(request, id): 
        membro = get_object_or_404(Membros,  id=id)
        if request.method == "POST":
           membro.delete() 
        return redirect('lista_membros'),

        return render(request, "confirmar_delecao.html", {"membro": membro})
