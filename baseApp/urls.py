from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.log_out, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
