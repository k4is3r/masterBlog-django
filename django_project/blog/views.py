from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'edward',
        'title':'Blog Post 1',
        'content':'Frist post content',
        'date_posted':'December 1, 2019'
    },
    {
        'author':'Oscar Carillo',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'December 3, 2019'
    },
    {
        'author':'Samantha Ricardo',
        'title':'Blog Post 3',
        'content':'Third post content',
        'date_posted':'December 5, 2019'
    },
    {
        'author':'Lucero Martinez',
        'title':'Blog Post 4',
        'content':'Frourt post content',
        'date_posted':'December 8, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})