from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path('signin', views.signin, name = 'signin'),
    path('register', views.register, name = 'register'),
    path('enter', views.enter, name = 'enter'),
    path('home', views.home, name = 'home'),
    path('logout', views.logout, name = 'logout'),
    path('supuser', views.supuser, name = 'supuser'),
    path('new', views.create_product, name = 'create_product'),
    path('update/<int:id>/', views.update_product, name = 'update_product'),
    path('delete/<int:id>/', views.delete_product, name = 'delete_product'),    
    path('search', views.admin_search, name = 'admin_search'),

]