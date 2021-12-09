from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    employee_id = models.TextField(unique=True, blank=False)
    password = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.employee_id

class Dealer(models.Model):
    dealer_id = models.TextField(unique=True, blank=False)
    password = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.dealer_id

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    enrollment_id = models.TextField()
    password = models.TextField()
    total_amount = models.IntegerField()
    name = models.TextField()
    father_name = models.TextField()
    landmark = models.TextField()
    village_ward = models.TextField()
    post_office = models.TextField()
    city = models.TextField()
    district = models.TextField()
    state = models.TextField()
    pin = models.IntegerField()
    due_cleared = models.BooleanField(default=False, blank=True)
    landmark = models.TextField()
    phone_number = models.TextField()
    aadhaar_number = models.IntegerField(max_length=12)
    pan_number = models.TextField(max_length=10)
    aadhaar_image = models.ImageField(upload_to="aadhaar_images")
    pan_image = models.ImageField(upload_to="pan_images")
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True, blank=True)
    admin = models.TextField(null=True, blank=True)
    status = models.TextField(default="pending", blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.TextField()
    subject = models.TextField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.subject + " - " + self.name

class EMI(models.Model):
    enrollment_id = models.TextField()
    amount = models.IntegerField(default=0)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.enrollment_id + " - " + self.amount

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_dealer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username