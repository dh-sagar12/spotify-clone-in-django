from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import deactivate
from .logic_functions import *
from .models import Music
import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home (request):
    time_period = get_time_period()
    latestTime = datetime.date.today() - datetime.timedelta(days=3)
    music = Music.objects.all()
    newRelease = Music.objects.filter(upload_date__gte = latestTime)[:4]
    params = {
        'user': request.user,
        'time_period': time_period,
        'music': music,
        'new_release': newRelease
    }

    return render(request, 'home/home.html' , params)



@login_required(login_url='login')
def addNewSong(request):
    if request.user.is_artist == True:
        if request.method == 'POST':
            name = request.POST.get('name')
            artist = request.POST.get('artist')
            genre = request.POST.get('genre')
            musicFile = request.FILES['musicFile']
            imageFile = request.FILES['imageFile']
            music_obj = Music.objects.create(name=name, uploader=request.user,  artist=artist, genre=genre, music_file= musicFile, music_cover_photo= imageFile)
            music_obj.save()
            success = str('Music Successfuly Added!!!')
            return render(request, 'home/addsong.html', {'success': success}) 
        return render(request, 'home/addsong.html')
    
    else:
        message = {'title': 'Cannot Upload a Song', 
                   'message': 'You must have a artist account to upload a song. You can process for artist account by clicking the button below'
                   }
        return  render(request, 'home/addsong.html',{'message': message})
    