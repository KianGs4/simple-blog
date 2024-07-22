from django.shortcuts import render
from django.http import HttpResponse

posts = [ 
    {
        'author': 'CoreyMs', 
        'title' : 'nmd post', 
        'content': "first post i have", 
        'data_posted': 'june 21, 2024'
    }, 
    {
        'author': 'mia', 
        'title' : 'nmd post', 
        'content': "second post i have", 
        'data_posted': 'june 25, 2024'
    }
]

def home(request): 
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request): 
    return render(request, 'blog/about.html', {'title': 'about'} )