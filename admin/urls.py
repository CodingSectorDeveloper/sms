from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('dealers/', views.dealers, name="dealers"),
    path('create_dealer/', views.create_dealer, name="create_dealer"),
    path('enrollments/', views.enrollments, name="enrollments"),
    path('create_enrollment/', views.create_enrollment, name="create_enrollment"),
    path('approval/', views.approval, name="approval"),
    path('profit_loss/', views.profit_loss, name="profit_loss"),
    path('employee/', views.employee, name="employee"),
    path('emi/', views.emi, name="emi"),
    path('submit_emi/', views.submit_emi, name="submit_emi"),
    path('messages/', views.messages, name="messages"),
    path('message_details/<int:id>', views.message_details, name="message_details"),
    path('approve/<int:id>', views.approve, name="approve"),
    path('reject/<int:id>', views.reject, name="reject"),
    path('approval_details/<int:id>', views.approval_details, name="approval_details"),
    path('enrollment_details/<int:id>', views.enrollment_details, name="enrollment_details"),
    path('delete_dealer/<int:id>', views.delete_dealer, name="delete_dealer"),
    path('delete_message/<int:id>', views.delete_message, name="delete_message"),
]
