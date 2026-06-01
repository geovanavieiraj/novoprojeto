from django.contrib import admin
from django.urls import path
from app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_senhas, name='lista_senhas'),
    path('novo/', views.adicionar_senha, name='adicionar_senha'),
]