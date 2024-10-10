from django.contrib import admin
from django.urls import path
from dispositivos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dispositivos/', views.home),
    path('dispositivos/add', views.cadastro, name='addDevice'),
    path('dispositivos/list', views.listagem, name='listDevices'),
    path('dispositivos/del', views.excluir, name='delDevice'),
    path('dispositivos/upd/<int:id>/', views.atualizar, name='updDevice'),
    path('acoes/list/<int:id>/', views.listagemAcoes, name='listActions'),
    path('acoes/add/<int:id>/', views.cadastroAcao, name='addAction'),
    path('acoes/del', views.excluirAcao, name='delAction'),
    path('acoes/upd/<int:id>/', views.atualizarAcao, name='updAction'),
    path('dispositivos/scanner', views.completeScan, name='scanDevices'),
]
