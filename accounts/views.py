from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages


# Create your views here.


@login_required(login_url='login')
def showProfile(request, username):
    getuser = User.objects.get(username=username)
    params = {'getuser': getuser}
    return render(request, 'accounts/profile.html', params)




@login_required(login_url = 'login')
def editProfile(request):
    user = User.objects.filter(username= request.user.username)
    thisuser= user.first()
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        about = request.POST.get('about')
        birthDay = request.POST.get('birthDay')
        birthMonth = request.POST.get('birthMonth')
        birthYear = request.POST.get('birthYear')
        facebookLink = request.POST.get('facebookLink')
        instagramLink = request.POST.get('instagramLink')
        twitterLink = request.POST.get('twitterLink')
        youtubeLink = request.POST.get('youtubeLink')
        webLink = request.POST.get('webLink')
        avatar = request.FILES.get('avatar')
        dateOfBirth = get_mdy_date(int(birthYear), int(birthMonth), int(birthDay))
        
        print(avatar, firstName, lastName, email, about, birthYear, birthMonth, birthDay, facebookLink, instagramLink, twitterLink, youtubeLink, webLink)
        if avatar != None:
            thisuser.avatar = avatar
            user.update(first_name= firstName, last_name=lastName, email=email, about=about, insta_link=instagramLink, facebook_link=facebookLink, twitter_link=twitterLink, youtube_link= youtubeLink, external_link= webLink, date_of_birth= dateOfBirth )
            thisuser.save()
        else:
            user.update(first_name= firstName, last_name=lastName, email=email, about=about, insta_link=instagramLink, facebook_link=facebookLink, twitter_link=twitterLink, youtube_link= youtubeLink, external_link= webLink, date_of_birth= dateOfBirth )
            
        messages.success(request,"Profile Updated Successfully")
        # return render(request, 'accounts/editprofile.html', {'message': message, 'user': thisuser})
        return redirect(reverse(editProfile))
        
    return render(request, 'accounts/editprofile.html')


def get_mdy_date(year, month, day):
    dob =  datetime.date(year, month, day)
    return dob