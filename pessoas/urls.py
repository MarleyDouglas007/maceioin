# pessoas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_pessoas/', views.list_pessoas, name='list_pessoas'),
    path('add_pessoa/', views.add_pessoa, name='add_pessoa'),
    path('edit_pessoa/<int:pessoa_id>/', views.edit_pessoa, name='edit_pessoa'),
    path('delete_pessoa/<int:pessoa_id>/', views.delete_pessoa, name='delete_pessoa'),
]
