from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts, name='blog-main'),
    path('post/<str:pk>/', views.post, name='blog-post'),

    path('create_post/', views.create_post, name='create_post')
]
