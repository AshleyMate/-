from django.urls import path
from wordcount import views

app_name = 'wordcount'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('count/', views.count, name='count'),
]
