from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path("home.html", views.home, name="home"),
    path("dietplan.html", views.dietplan, name="dietplan"),
    path("footballdrills.html", views.footballdrills, name="footballdrills"),
    path("strength.html", views.strength, name="strength"),
    path("logfood.html", views.logfood, name="logfood"),
    path("recovery.html", views.recovery, name="recovery"),
    path("calender.html", views.calender, name="calender"),
    path("wellbeing.html", views.wellbeing, name="wellbeing"),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

]