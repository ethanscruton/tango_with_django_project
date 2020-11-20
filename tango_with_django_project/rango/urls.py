from django.conf.urls import url
from django.urls import path
from rango import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<str:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<str:category_name_slug>/add_page/', views.add_page, name='add_page'),
]