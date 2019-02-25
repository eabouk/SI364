from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.MainView.as_view(), name='cats'),
    path('main/create/', views.CatsCreate.as_view(), name='cats_create'),
    path('main/<int:pk>/update/', views.CatsUpdate.as_view(), name='cats_update'),
    path('main/<int:pk>/delete/', views.CatsDelete.as_view(), name='cats_delete'),
    path('lookup/', views.CatsView.as_view(), name='cats_list'),
    path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]