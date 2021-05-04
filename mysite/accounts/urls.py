"""
Account navigation paths
"""
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.signin, name='signin'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
