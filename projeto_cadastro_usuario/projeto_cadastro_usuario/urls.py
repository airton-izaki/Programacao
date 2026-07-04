
from django.contrib         import admin
from django.urls            import path
from app_cadastro_usuarios  import views

urlpatterns = [
    # Rota, View responsável,   Nome de referência
    path(
        '', 
        views.home,
        name = 'home'
    ),

    path(
        'usuarios/', 
        views.usuarios,
        name = 'listagem_usuarios'
    )
]
