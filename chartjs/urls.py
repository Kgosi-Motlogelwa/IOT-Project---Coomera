from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    #path('data', views.data, name = 'data')
    path('api', views.ChartData.as_view()), 
]