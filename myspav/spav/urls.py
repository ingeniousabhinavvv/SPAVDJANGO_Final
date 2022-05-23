from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
    path('tender/', views.tender, name='tender'),
    path('gallery/', views.gallery, name='gallery'),
]
