from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from main.models import *

def home(request):
    return render(request, "Employee/home.html")

def approval(request):
    enrollments = Enrollment.objects.filter(status="pending")
    return render(request, "Employee/approval.html", {"enrolls":enrollments})

def approval_details(request, id):
    enroll = Enrollment.objects.filter(pk=id).last()
    return render(request, "Employee/approval_details.html", {"enroll":enroll})

def reject(request, id):
    enroll = Enrollment.objects.filter(pk=id).last()
    enroll.status = "rejected"
    enroll.save()
    return HttpResponseRedirect("/employee_dashboard/approval")

def approve(request, id):
    enroll = Enrollment.objects.filter(pk=id).last()
    enroll.status = "approved"
    enroll.save()
    return HttpResponseRedirect("/employee_dashboard/approval")