# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *



def index(request):
    return render(request, 'login_app/index.html')

def login(request):
    user = User.objects.login(request.POST)
    if user:
        request.session['user_id'] = user.id
        current_id = request.session[user.id]
        return redirect('/home')

    messages.error(request, "Login incorrect")  
    return redirect('/')

def quotes(request):
    user_id = {
        'user_id': request.session['user_id']
    }
    return render(request, 'quotes/index.html', user_id)

def registration(request):
    res = User.objects.userIsValid(request.POST)
    if res['status']:
        user = User.objects.createUser(request.POST)
        request.session['user_id'] = user.id
        return redirect('/home')
        print 'valid user'
    else:
        for error in res['errors']:
            messages.error(request, error)  
            # error is a tag. Tags can be error, success, etc. Can be manipulated further like changing colors          
        print res['errors']
    return redirect('/')

def home(request):
    if 'user_id' not in request.session:
        return redirect('/')
    userData = {
        'user': User.objects.get(id = request.session['user_id']),
        'quotes': Quotes.objects.filter(user_id = request.session['user_id'])
    }
    print request.session['user_id']
    print userData
    return render(request, 'login_app/home.html', userData)




# Create your views here.
