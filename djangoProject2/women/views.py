from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import AddPostForm
from .models import *


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить пост', 'url_name': 'add_post'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


def main(request):
    posts = Women.objects.all()
    context = {
        'title': 'Главная',
        'posts': posts,
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    context = {
        'title': 'Добавить пост',
        'cat_selected': 0,
        'form': form
    }
    return render(request, 'women/addPost.html', context=context)


def contact(request):
    return HttpResponse('Связаться с нами')


def about(request):
    context = {
        'title': 'О сайте',
        'cat_selected': 0
    }
    return render(request, 'women/about.html', context=context)


def show_post(request, slug_url):
    women = get_object_or_404(Women, slug=slug_url)
    context = {
        'title': women.title,
        'women': women,
        'cat_selected': women.cat_id
    }
    return render(request, 'women/post.html', context=context)


def show_category(request, slug_url):
    category = get_object_or_404(Category, slug=slug_url)
    women = Women.objects.filter(cat_id=category.pk)
    if len(women) == 0:
        raise Http404()
    context = {
        'title': 'Категория',
        'posts': women,
        'cat_selected': category.pk
    }
    return render(request, 'women/index.html', context=context)


def login(request):
    return HttpResponse('Авторизироваться')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')