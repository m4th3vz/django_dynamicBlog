# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    # Página de lista dos posts
    path('listText/', views.listText, name='listText'),
    # Página para publicar post
    path('postText/', views.postText, name='postText'),
    # Página dinâmica para ler os posts
    path('detailText/<int:texto_id>/', views.detailText, name='detailText'),
    # Página para excluir post
    path('deleteText/<int:texto_id>/', views.deleteText, name='deleteText'),
]
