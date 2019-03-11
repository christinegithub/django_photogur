from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment
from photogur.forms import LoginForm


def picture_page(request):
    context = {'pictures': Picture.objects.all() }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def picture_show(request, id):
    picture = Picture.objects.get(pk = id)
    context = {'picture': picture}
    response = render(request, 'picture.html', context)
    return HttpResponse(response)

def picture_search(request):
    query = request.GET['query']
    search_results = Picture.objects.filter(artist__contains=query) | Picture.objects.filter(title__contains=query) | Picture.objects.filter(url__contains=query)
    context = {'pictures': search_results, 'query': query}
    response = render(request, 'picture_search.html', context)
    return HttpResponse(response)

def create_comment(request):
    picture = request.POST['picture']
    comment_name = request.POST['comment-name']
    comment_message = request.POST['comment-message']
    comment = Comment.objects.create(picture=Picture.objects.get(id=picture), name=comment_name, message=comment_message)
    return HttpResponseRedirect('/pictures/'+ picture)

def login_view(request):
    form = LoginForm()
    context = {'form': form}
    response = render(request, 'login.html', context)
    return HttpResponse(response)
