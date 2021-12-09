from django.shortcuts import render, HttpResponse
import random
import string
from main.models import *

def home(request):
    enrollnum = len(Enrollment.objects.filter(dealer=Dealer.objects.filter(user=request.user).last()))
    eminum = len(EMI.objects.filter(dealer=Dealer.objects.filter(user=request.user).last()))
    return render(request, "Dealer/home.html", {"enroll":enrollnum, "emi":eminum})

def enrollments(request):
    enrollments = Enrollment.objects.filter(dealer=Dealer.objects.filter(user=request.user).last())
    return render(request, "Dealer/enrollments.html", {"enrollments":enrollments})

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
        dealer = None
        if UserDetails.objects.filter(user=request.user).last().is_dealer:
            dealer = Dealer.objects.filter(user=request.user).last()
        username = name
        if ' ' in name:
            username = name.replace(" ","")
            print(username)
        if same:
            user_created = User.objects.filter(email=email, username=username).last()
            enroll_created = Enrollment.objects.create(user=user_created , enrollment_id=id_created,password=password, name=name, father_name=father, phone_number=contact,landmark=landmark, village_ward=village_ward, post_office=post_office,city=city, pin=pin, aadhaar_number=aadhaar_number,aadhaar_image=aadhaar_image, state=state,pan_number=pan_number,pan_image=pan_image, dealer=dealer, total_amount=amount, district=district)
            return render(request, "Dealer/create_enrollment.html", {"success":True})
        else:
            user_created = User.objects.create_user(email=email,password=password, username=username)
            user_detail = UserDetails.objects.create(user=user_created, is_customer=True)
            enroll_created = Enrollment.objects.create(user=user_created , enrollment_id=id_created,password=password, name=name, father_name=father, phone_number=contact,landmark=landmark, village_ward=village_ward, post_office=post_office,city=city, pin=pin, aadhaar_number=aadhaar_number,aadhaar_image=aadhaar_image, state=state,pan_number=pan_number,pan_image=pan_image, dealer=dealer, total_amount=amount, district=district)
            return render(request, "Dealer/create_enrollment.html", {"success":True})

    return render(request, "Dealer/create_enrollment.html", {"id":id_created})

def enrollment_details(request, id):
    enrollment = Enrollment.objects.filter(pk=id).last()
    return render(request, "Dealer/enrollment_details.html", {"enrollment":enrollment})

def submit_emi(request):
    if request.method == 'POST':
        enrollment_id = request.POST['id']
        amount = request.POST['amount']
        dealer = Dealer.objects.filter(user=request.user).last()
        emi = EMI.objects.create(enrollment_id=enrollment_id, amount=amount, dealer=dealer)
        return render(request, "Dealer/submit_emi.html", {"success":True})
    return render(request, "Dealer/submit_emi.html")

def emi(request):
    emis = EMI.objects.filter(dealer=Dealer.objects.filter(user=request.user).last())
    return render(request, "Dealer/emi.html", {"emis":emis})