from django.contrib import admin
from django.urls import path
from dispositivos import views
from autenticacao import views as autviews
from rest_framework.authentication.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('login/', autviews.login),
    # path('admin/', admin.site.urls),
    path('dispositivos/', views.home),
    path('dispositivos/add', views.cadastro, name='addDevice'),
    path('dispositivos/list', views.listagem, name='listDevices'),
    path('dispositivos/del', views.excluir, name='delDevice'),
    path('dispositivos/upd/<int:id>/', views.atualizar, name='updDevice'),
    path('acoes/list/<int:id>/', views.listagemAcoes, name='listActions'),
    path('acoes/add/<int:id>/', views.cadastroAcao, name='addAction'),
    path('acoes/del', views.excluirAcao, name='delAction'),
    path('acoes/upd/<int:id>/', views.atualizarAcao, name='updAction'),
    path('dispositivos/scanner', views.scanDevices, name='scanDevices'),
    path('dispositivos/unico/<int:id>/', views.dispositivoUnico, name='scanDevices'),
]
