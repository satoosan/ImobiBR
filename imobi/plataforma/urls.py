from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name="home"),
    path('imovel/<str:id>', views.imovel, name="imovel"),
    path('agendar_visitas', views.agendar_visitas, name="agendar_visitas"),
    path('agendamentos', views.agendamentos, name="agendamentos"),
    path('cancelar_agendamento/<str:id>',
         views.cancelar_agendamento, name="cancelar_agendamento"),
    path('limpar_agendamento/<str:id>',
         views.limpar_agendamento, name="limpar_agendamento"),
    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),
]
