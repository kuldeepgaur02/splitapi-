
from django.contrib import admin

from django.contrib.auth import views as auth_views

from django.urls import path, include

from kuldeepAPI import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.homePage),
    
    path('register/', views.register_user, name='register'),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('profile/', views.user_profile, name='profile'),
    
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    
    path('add_user/', views.add_user, name='add_user'),
    
    path('add_expense/', views.add_expense),
    
    path('expenses/', views.show_expenses, name='show_expenses'),
    
    path('expenses/<int:user_id>/', views.show_expenses, name='user_expenses'),
    
    path('download_balance_sheet/', views.download_balance_sheet, name='download_balance_sheet'),
]
