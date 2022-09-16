from django.urls import path
from LoginApp import views
#from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('dashboard/',views.home),
	path('', views.user_login),
	path('logout',views.logout_call),
	path('login/', views.user_login,name='LoginApp'),
	path('Create_User',views.Create_User, name='Create_User'),
	
   


	]
	
	