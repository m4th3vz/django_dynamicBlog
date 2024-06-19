from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listText/', views.listText, name='listText'),
    path('postText/', views.postText, name='postText'),
    path('detailText/<int:texto_id>/', views.detailText, name='detailText'),
]
