from django.urls import path
from . import views


urlpatterns = [
    path('', views.userLogin, name= 'Login'),
    path('register/', views.userRegistrtion, name= 'Registration'),
    path('category/', views.categoryManagement, name= 'categoryManagement'),
    path('logout/', views.logout, name= 'Logout'),
    path('delete/<id>', views.deleteCategory, name= 'DeleteCategory'),
]

