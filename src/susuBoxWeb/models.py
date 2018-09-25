from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.TextField(max_length=100000)
    answer = models.TextField(max_length=100000)

    def __str__(self):
        return self.question

class Terms(models.Model):
    header = models.TextField(max_length=100000)
    body = models.TextField(max_length=1000000)

    def __str__(self):
        return self.header

class PrivacyPolicy(models.Model):
    header = models.TextField(max_length=1000000)
    body = models.TextField(max_length=1000000)

class TypeOfCard(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Currency(models.Model):
    type = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.type}({self.symbol})"

class Account(models.Model):
    accountName = models.TextField() #Should be encrypted
    accountNumber = models.TextField() #Should be encrypted
    securityCode = models.TextField() #Should be encrypted
    expiryDate = models.DateField() #Should be encrypted
    typeOfCardId = models.ForeignKey(TypeOfCard, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class EmploymentStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Customer(models.Model):
    email = models.EmailField() #encrypted
    phoneNumber = models.TextField() #encrypted
    password = models.TextField()
    genderId = models.ForeignKey(Gender, on_delete=models.CASCADE)
    dateOfBirth = models.DateField()
    employmentStatusId = models.ForeignKey(EmploymentStatus, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Banks(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name

class SavingsDuration(models.Model):
    DurationName = models.CharField(max_length=255)
    NumOfDays = models.IntegerField()

    def __str__(self):
        return self.DurationName

class SusuBox(models.Model):
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    savingsAmount = models.DecimalField(max_digits=1000, decimal_places=2)
    savingsDate = models.DateField()
    lastRenewalDate = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class SusuHistory(models.Model):
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lastLoginDate = models.DateField()
    lastSavingsDate = models.DateField()
    lastSavingsAmount = models.DecimalField(max_digits=1000, decimal_places=2)
    successFul = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

