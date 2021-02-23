from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import PhotoForm
from django.core.paginator import Paginator


def home(request):

    search_quaries = filters(request)
    if search_quaries:
        photos = search_quaries
    else:
        photos = Photo.objects.filter(published=True).order_by('-created')

    paginator = Paginator(photos, 16)
    page_number = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_number)

    context = {
        'photos': photos,
        'page_objects':page_objects,
    }
    return render(request, 'photos/index.html', context)


def post(request):
    form = PhotoForm()
    if request.method == 'POST':
        data = request.POST
        
        post = Photo(user=request.user, preview_text=data['preview_text'], title=data['title'], 
        description=data['description'], tag=data['tag'],
         thumbnail=data['thumbnail'],published=True)

        post.save()
        return redirect('home')

    context = {
        'form':form
    }
    
    return render(request, 'photos/post.html', context)


def detail(request, slug):
    photo = Photo.objects.get(slug=slug)

    context = {
        'photo' : photo
    }
    
    return render(request, 'photos/single.html', context)



def filters(request):
    if request.method == 'POST':
        data = request.POST
        photos = Photo.objects.filter(published=True, preview_text__contains=data['Search'])
    else:
        photos = Photo.objects.filter(published=True).order_by('-created')
    
    return photos
