from django.urls import path

from . import views

app_name = 'bootstrap_template'

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
