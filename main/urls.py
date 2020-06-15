from django.urls import path

from main import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('skill/<str:title>/', views.skill_view, name='skill')
]
