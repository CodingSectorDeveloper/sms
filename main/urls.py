from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('customer/', views.customer, name="customer"),
    path('employee/', views.employee, name="employee"),
    path('login/', views.login, name="login"),
    path('dealer_login/', views.dealer_login, name="dealer_login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
