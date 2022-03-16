from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name='sair')
]

#error404
handler404 = "autenticacao.views.handler404"

#error server
handler500 = 'autenticacao.views.handler500'
handler501 = 'autenticacao.views.handler500'
handler502 = 'autenticacao.views.handler500'
handler503 = 'autenticacao.views.handler500'
handler504 = 'autenticacao.views.handler500'
handler505 = 'autenticacao.views.handler500'