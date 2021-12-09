import random
import string
from django.shortcuts import render, HttpResponseRedirect
from main.models import *

# Create your views here.

def home(request):
    dealernum = len(Dealer.objects.all())
    msgnum = len(Message.objects.all())
    enrollnum = len(Enrollment.objects.all())
    invested = 0
    for i in Enrollment.objects.all():
        invested += i.total_amount
    invested = "{:,}".format(invested)
    income = 0
    for i in EMI.objects.all():
        income += i.amount
    income = "{:,}".format(income)
    users = len(User.objects.all())
    return render(request, "Admin/home.html", {"dealernum":dealernum,"msgnum":msgnum, "enrollnum":enrollnum, "invested":invested, "users":users, "income":income})

def dealers(request):
    dealer = Dealer.objects.all()
    response = render(request, "Admin/dealers.html", {"dealers":dealer})
    response.set_cookie("test_cookie", "This is the test", max_age=60*60*24*14)
    return response

def create_dealer(request):
    id_created = ''.join(random.choice(string.digits) for _ in range(6))
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        if ' ' in name:
            return render(request, "Admin/create_dealer.html", {"error":True, "message":"Username Cannot Contain Space", "id":id_created})
        elif User.objects.filter(username=name, password=password).exists():
            return render(request, "Admin/create_dealer.html", {"error":True, "message":"Same User Already Exists", "id":id_created})
        else:
            user_created = User.objects.create_user(username=name, email=email, password=password)
            user_detail = UserDetails.objects.create(user=user_created, is_dealer=True)
            dealer_created = Dealer.objects.create(dealer_id=id_created, password=password, user=user_created)
            return render(request, "Admin/create_dealer.html", {"success":True})
    return render(request, "Admin/create_dealer.html", {"id":id_created})

def delete_dealer(request, id):
    dealer = Dealer.objects.filter(pk=id).last()
    dealer.delete()
    return HttpResponseRedirect("/admin_dashboard/dealers")

def enrollment_details(request, id):
    enrollment = Enrollment.objects.filter(pk=id).last()
    return render(request, "Admin/enrollment_details.html", {"enrollment":enrollment})
    
def enrollments(request):
    enrollments = Enrollment.objects.all()
    return render(request, "Admin/enrollments.html", {"enrollments":enrollments})

def approval(request):
    enrollments = Enrollment.objects.filter(status="pending")
    return render(request, "Admin/approval.html", {"enrolls":enrollments})

def approval_details(request, id):
    enroll = Enrollment.objects.filter(pk=id).last()
    return render(request, "Admin/approval_details.html", {"enroll":enroll})

def reject(request, id):
    enroll = Enrollment.objects.filter(pk=id).last()
    enroll.status = "rejected"
    enroll.save()
    return HttpResponseRedirect("/admin_dashboard/approval")

def approve(request, id):
    enroll = Enrollment.objects.filter(pk=id).last()
    enroll.status = "approved"
    enroll.save()
    return HttpResponseRedirect("/admin_dashboard/approval")

def messages(request):
    messages = Message.objects.all()
    return render(request, "Admin/messages.html", {"messages":messages})

def message_details(request, id):
    message = Message.objects.filter(pk=id).last()
    return render(request, "Admin/message_details.html", {"message":message})

def delete_message(request, id):
    Message.objects.filter(pk=id).last().delete()
    return HttpResponseRedirect("/admin_dashboard/messages")

def emi(request):
    emis = EMI.objects.all()
    return render(request, "Admin/emi.html", {"emis":emis})

def profit_loss(request):
    invested_num = 0
    for i in Enrollment.objects.all():
        invested_num += i.total_amount
    invested = "{:,}".format(invested_num)
    income_num = 0
    for i in EMI.objects.all():
        income_num += i.amount
    income = "{:,}".format(income_num)
    profit = 0
    loss = 0
    if invested_num > income_num:
        loss = invested_num - income_num
    elif income_num > invested_num:
        profit_num = income - invested_num
    profit = "{:,}".format(profit)
    loss = "{:,}".format(loss)
    emi = EMI.objects.all()
    return render(request, "Admin/profit_loss.html", {"investment":invested,"emis":emi,  "income":income, "profit":profit, "loss":loss})

def employee(request):
    employee = Employee.objects.all()
    return render(request, "Admin/employee.html", {"employee":employee})

def create_enrollment(request):
    id_created = ''.join(random.choice(string.digits) for _ in range(6))
    if request.method == 'POST':
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        father = request.POST['father']
        contact = request.POST['contact']
        landmark = request.POST['landmark']
        village_ward = request.POST['village_ward']
        post_office = request.POST['post_office']
        city = request.POST['city']
        amount = request.POST['amount']
        pin = request.POST['pin']
        aadhaar_number = request.POST['aadhaar_number']
        aadhaar_image = request.FILES['aadhaar_image']
        pan_number = request.POST['pan_number']
        state = request.POST['state']
        same = request.POST.get('same')
        print(same)
        pan_image = request.FILES['pan_image']
        district= request.POST['district']
        admin = request.user
        username = name
        if ' ' in name:
            username = name.replace(" ","")
            print(username)
        if Enrollment.objects.filter(phone_number=contact, due_cleared=False).exists():
            return render(request, "Admin/create_enrollment.html", {"error": True, "message":"Same Enrollment Exists", "id":id_created})
        else:
            if same:
                user_created = User.objects.filter(email=email, username=username).last()
                enroll_created = Enrollment.objects.create(user=user_created , enrollment_id=id_created,password=password, name=name, father_name=father, phone_number=contact,landmark=landmark, village_ward=village_ward, post_office=post_office,city=city, pin=pin, aadhaar_number=aadhaar_number,aadhaar_image=aadhaar_image, state=state,pan_number=pan_number,pan_image=pan_image, admin=admin, total_amount=amount, district=district)
                return render(request, "Admin/create_enrollment.html", {"success":True})
            else:
                user_created = User.objects.create_user(email=email,password=password, username=username)
                user_detail = UserDetails.objects.create(user=user_created, is_customer=True)
                enroll_created = Enrollment.objects.create(user=user_created , enrollment_id=id_created,password=password, name=name, father_name=father, phone_number=contact,landmark=landmark, village_ward=village_ward, post_office=post_office,city=city, pin=pin, aadhaar_number=aadhaar_number,aadhaar_image=aadhaar_image, state=state,pan_number=pan_number,pan_image=pan_image, admin=admin, total_amount=amount, district=district)
                return render(request, "Admin/create_enrollment.html", {"success":True})

    return render(request, "Admin/create_enrollment.html", {"id":id_created})

def submit_emi(request):
    if request.method == 'POST':
        enrollment_id = request.POST['id']
        amount = request.POST['amount']
        admin = request.user
        emi = EMI.objects.create(enrollment_id=enrollment_id, amount=amount, admin=admin)
        return render(request, "Admin/submit_emi.html", {"success":True})
    return render(request, "Admin/submit_emi.html")