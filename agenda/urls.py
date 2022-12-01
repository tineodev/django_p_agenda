from django.urls import path
from agenda import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.page_contactos, name='list_contactos'),
    path('contacts_add/', views.page_add_contacto, name='add_contacto'),
    path('contacts_detail/', views.page_detail_contacto, name='detail_contacto'),
]