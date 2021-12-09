from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('enrollments/', views.enrollments, name="enrollments"),
    path('submit_emi/', views.submit_emi, name="submit_emi"),
    path('emi/', views.emi, name="emi"),
    path('create_enrollment/', views.create_enrollment, name="create_enrollment"),
    path('enrollment_details/<int:id>', views.enrollment_details, name="enrollment_details"),
]
