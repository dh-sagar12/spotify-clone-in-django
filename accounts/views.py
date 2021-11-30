from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def showProfile(request, username):
    getuser = User.objects.get(username=username)
    params = {'getuser': getuser}
    return render(request, 'accounts/profile.html', params)




@login_required(login_url = 'login')
def editProfile(request):
    if request.method == 'POST':
        pass
    
    return render(request, 'accounts/editprofile.html')