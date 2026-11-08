from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('blank/', views.blank, name='blank'),
    path('utilities/animation/', views.utilities_animation, name='utilities_animation'),
    path('utilities/border/', views.utilities_border, name='utilities_border'),
    path('utilities/color/', views.utilities_color, name='utilities_color'),
    path('utilities/other/', views.utilities_other, name='utilities_other'),
]
