# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    # Página da lista dos textos
    path('listText/', views.listText, name='listText'),
    # Página para publicar texto
    path('postText/', views.postText, name='postText'),
    # Página dinâmica para ler os textos
    path('detailText/<int:texto_id>/', views.detailText, name='detailText'),
    # Página para excluir texto
    path('deleteText/<int:texto_id>/', views.deleteText, name='deleteText'),
    # Página para editar texto
    path('editText/<int:texto_id>/', views.editText, name='editText'),
]
