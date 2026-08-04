from django.urls import path

from . import views

urlpatterns = [
    path('', views.Listar_membros, name='listar_membros'),
    path('criar/', views.criar_membro, name='criar_membro'),
    path('editar/<int:id>/', views.editar_membro, name='editar_membro'),
    path('deletar/,int:id>/', views.deletar_membro, name='deletar_membro')
]
