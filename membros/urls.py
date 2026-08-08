from django.urls import path

from . import views

urlpatterns = [
    # Páginas principais
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('prices/', views.prices, name='prices'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # URLs para serviços (adicionadas)
    path('service/<str:service_name>/', views.service_detail, name='service_detail'),
    path('booking/<int:service_id>/', views.booking, name='booking'),
    
    # Páginas de CRUD de membros
    path('membros/', views.listar_membros, name='listar_membros'),
    path('membros/criar/', views.criar_membro, name='criar_membro'),
    path('membros/editar/<int:id>/', views.editar_membro, name='editar_membro'),
    path('membros/deletar/<int:id>/', views.deletar_membro, name='deletar_membro'),
]