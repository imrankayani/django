from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import get_nutrition_data

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
    path('nutrition', get_nutrition_data, name='nutrition_data'),

  

]