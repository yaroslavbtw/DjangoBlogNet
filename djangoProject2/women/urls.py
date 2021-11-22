from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('category/<slug:slug_url>/', show_category, name='show_category'),
    path('addpost/', add_post, name='add_post'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('post/<slug:slug_url>/', show_post, name='show_post')
]