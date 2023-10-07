from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='projects'),
    path('news/', views.news, name='news'),
    path('people/', views.people, name='people'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
]
