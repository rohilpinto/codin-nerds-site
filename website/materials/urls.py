from django.urls import path

from . import views

urlpatterns = [
    path('resources/', views.resources_show, name='coding-resources'),
    path('tools/', views.tools_show, name='coding-tools'),
    path('help/', views.help_show, name='coding-help'),
]
