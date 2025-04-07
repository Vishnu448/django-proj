from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from .views import register_user, login_view





urlpatterns=[
    path('index',views.index, name='index'),
    path('<str:slug>', views.detail, name='detail'), 
    path('new_url', views.new_url_redirect,name="new_url"),
    path('old_url', views.old_url_redirect,name="old_url"),
    path('contact/', views.contact_view,name="contact"),
    path('about/', views.about_view, name="about"),
    path('register/',views.register_page, name='register'),
    path('api/register/', views.register_user, name='api-register'), 
    path('',views.login_view, name='login'),
    
    
]