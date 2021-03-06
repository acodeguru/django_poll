"""
Polls navigation paths
"""
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.CreateView.as_view(), name='add'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', login_required(views.ResultsView.as_view()), name='results'),
    path('<int:question_id>/vote/', login_required(views.vote), name='vote'),
]
