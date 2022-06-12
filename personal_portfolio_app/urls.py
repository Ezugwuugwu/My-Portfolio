from django.urls import path

from personal_portfolio_app import views

urlpatterns = [
    path('home_portfolio', views.homepage),
]