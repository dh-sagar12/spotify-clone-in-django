import datetime
from django.shortcuts import redirect, render
from django.urls import reverse
from accounts.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from accounts.forms import UserCreationForm
from .models import VerificationToken
import uuid 
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


def loginView(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    else:
        if request.method== 'POST':
            email=  request.POST.get('username')
            password=  request.POST.get('password')
            usr = User.objects.filter(email=email).first()
            if usr:
                if usr.is_active:
                    authUser= authenticate(email= usr.email, password=password)
                    django_login(request, authUser)
                    if request.POST.get('next'):
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect(reverse('home'))
                else:
                    authentication_key = str(uuid.uuid4())
                    first_name = usr.first_name
                    invalid_multiple_token(request, usr)
                    verification_obj = VerificationToken.objects.create(user=usr, authentication_key= authentication_key)
                    verification_obj.save()
                    send_verification_mail(email,authentication_key, first_name )
                    return redirect(reverse('token'))
                    
                    
            else:
                params = {'error': 'Invalid Credentials'}
                return render(request, 'registration/login.html', params)
            
    return render(request, 'registration/login.html')

def logoutView(request):
    django_logout(request)
    return redirect(reverse('login'))


def createUser(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    else:
        form = UserCreationForm()
        params = {'form': form}
        
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                email =  request.POST.get('email')
                first_name = request.POST.get('first_name')
                user_obj = User.objects.get(email= email)
                print(user_obj)
                authentication_key = str(uuid.uuid4())
                verification_obj = VerificationToken.objects.create(user=user_obj, authentication_key= authentication_key)
                verification_obj.save()
                send_verification_mail(email,authentication_key, first_name )
                return redirect(reverse('token'))
            else:
                return render(request, 'registration/signup.html', {'form': form})
        
        return render(request, 'registration/signup.html', params )
        

def token_send(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    else:
        return render(request, 'registration/token_send.html')



def success(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    else:
        return render(request, 'registration/success.html')



def send_verification_mail(email, authentication_key, first_name):
    subject = 'Verify your email before logging in to songIT'
    message = f'Hi {first_name}. Thank you for joining songIT community.\n please click the link to verify yourself http://http://127.0.0.1:8000/auth/verify/{authentication_key} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list )

def verify(request, authentication_key):
    invalid_older_token(request)
    verification_obj = VerificationToken.objects.filter(authentication_key= authentication_key , is_valid= True).first()
    print(verification_obj)
    if verification_obj:
        if verification_obj.user.is_active:
            return render(request, 'registration/already_verified.html' )
        else:
            verification_obj.user.is_active = True
            verification_obj.user.save()
            return redirect(reverse('success'))
    
    else:
        return render(request, 'registration/expiretoken.html')
    
    

def invalid_older_token(request):
    validTime = datetime.date.today() - datetime.timedelta(hours=2)
    old_verification_tokens =  VerificationToken.objects.filter(created_on__lte= validTime)
    for i in old_verification_tokens:
        i.is_valid = False
        i.save()
    
def invalid_multiple_token(request, user):
    tokens = VerificationToken.objects.filter(user=user, is_valid= True)
    for token in tokens:
        token.is_valid = False
        token.save()