from django.shortcuts import render
from main.models import *

def home(request):
    return render(request, "Customer/home.html")

def emi(request):
    enroll_id = Enrollment.objects.filter(user=request.user).last().enrollment_id
    emis = EMI.objects.filter(enrollment_id=enroll_id)
    return render(request, "Customer/emi.html", {"emis":emis})