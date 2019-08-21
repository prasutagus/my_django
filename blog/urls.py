from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('blog/new', views.post_create, name='post_create'),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
