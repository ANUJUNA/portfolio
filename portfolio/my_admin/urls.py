from django.urls import path
from my_admin import views

urlpatterns = [
    path('', views.login, name='login'),
    path('check', views.check, name='check'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('logout/', views.logout, name='logout'),
]
