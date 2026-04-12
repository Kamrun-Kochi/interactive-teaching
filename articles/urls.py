from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('article/<int:pk>/', views.article_detail, name='detail'),
    path('media/<int:media_id>/popup/', views.media_popup, name='popup'),
]