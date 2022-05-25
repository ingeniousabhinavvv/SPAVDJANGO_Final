from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
    path('tender/', views.tender, name='tender'),
    path('gallery/', views.gallery, name='gallery'),
    path('convocation/', views.convocation, name='convocation'),
    path('faculty/', views.faculty, name='faculty'),
    path('upcominglectures/', views.upcominglectures, name='upcominglectures'),
    path('department-of-architecture/', views.doa, name='doa'),
]
