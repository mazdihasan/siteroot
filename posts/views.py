from django.shortcuts import render
from .models import Post
# Create your views here.


def blog(request):
    list_posts = Entry.objects.all()[:10]
    contex = {
        'articles' : list_posts
    }
    return render(request, 'index.html', contex)


def article(request, slug):
    contex = {

    }
    return render(request, 'single.html', contex)