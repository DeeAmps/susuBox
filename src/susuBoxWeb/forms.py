from django import forms
from .models import Banks, Gender, EmploymentStatus, TypeOfCard, SavingsDuration, Currency


class RegistrationForm(forms.Form):
    phoneNumber = forms.CharField(max_length=14,  widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    email = forms.CharField(widget= forms.EmailInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create a Password'}))
    dateOfBirth = forms.DateField(widget=forms.DateInput(attrs={'id' : 'dob', 'style' : 'width: 70%', 'type':'date'}))
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(),widget=forms.Select(attrs={'id':'gender'}))
    employmentStatus = forms.ModelChoiceField(queryset=EmploymentStatus.objects.all(),widget=forms.Select(attrs={'id':'employment'}))
    accountName = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder': ' First and Last Name(Should match that of Banks)'}))
    accountNumber = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder': 'Bank Account Number'}))
    typeOfCard = forms.ModelChoiceField(queryset=TypeOfCard.objects.all(),widget=forms.Select(attrs={'class':'toc', 'style':'margin-left:11%'}))
    expiryDate = forms.CharField(widget=forms.TextInput(attrs={'id': 'expiry', 'style' : 'width: 30%; margin-left: 10%', 'type':'text', 'placeholder' : 'mm/yy'}))
    cvv = forms.CharField(max_length=3,  widget=forms.TextInput(attrs={'id': 'cvv', 'type' : 'number', 'style':'width: 20%'}))
    bank = forms.ModelChoiceField(queryset=Banks.objects.all(),widget=forms.Select(attrs={'class':'toc', 'style':'margin-left:21%'}))
    savingsDuration = forms.ModelChoiceField(queryset=SavingsDuration.objects.all(),widget=forms.Select(attrs={'style':'width: 320px;margin-left: 18%'}))
    savingsBeginningDate = forms.DateField(widget=forms.DateInput(attrs={'id' : 'dob', 'style' : 'width: 65%', 'type':'date'}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={"style": "width: 40%"}))
    currency = forms.ModelChoiceField(queryset=Currency.objects.all(),widget=forms.Select(attrs={"style": "width: 30%;margin-left: 15%"}))

class LoginForm(forms.Form):
    phone_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number/Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class ResetPasswordForm(forms.Form):
    email = forms.CharField(widget= forms.EmailInput(attrs={'placeholder':'Kindly enter your email for your account'}))



