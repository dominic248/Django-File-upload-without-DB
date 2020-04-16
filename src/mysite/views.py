from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import time
import os

def return_page(request): 
    print(os.getenv("SECRET_KEY"))
    return HttpResponse("Success")

def home_page(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        # print(request.FILES['img'],request.FILES['img'].name,type(request.FILES['img']))
        timestr = time.strftime("%Y%m%d-%H%M%S")
        # print(timestr)
        data = request.FILES['img']
        path = default_storage.save('tmp/image-'+timestr+'.jpg', ContentFile(data.read()))
        return HttpResponseRedirect(reverse('return') )
    return render(request, 'home.html')
