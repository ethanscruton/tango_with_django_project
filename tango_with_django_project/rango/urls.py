from django.urls import path
from rango import views
from rango.views import UserListView, PageListView, AddCategoryView, AddPageView, IndexView, RegisterProfileView, EditProfileView

app_name = 'rango'
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('category/<str:category_name_slug>/', PageListView.as_view(), name='show_category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('goto/', views.track_url, name='goto'),
    path('category/<str:category_name_slug>/add_page/', AddPageView.as_view(), name='add_page'),
    path('logout/', views.user_logout, name='logout'),
    path('add_profile/', RegisterProfileView.as_view(), name='register_profile'),
    path('profile/<slug:user_slug>', EditProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='users'),
    path('like/', views.like_category, name='like_category'),
    path('suggest/', views.suggest_category, name='suggest_category')
]