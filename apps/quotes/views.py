# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    quotes = {
        'quotes': Quotes.objects.all()
    }
    print quotes
    return render(request, 'quotes/index.html', quotes)

def newQuote(request):
    res = Quotes.objects.quoteVal(request.POST)
    if res['status']:
         print "Adding quote"
         newQuote = Quotes.objects.newQuote(request.POST)
         return redirect('/quotes')
    else:
        for error in res['quoteErrors']:
            messages.error(request, error)  
            # error is a tag. Tags can be error, success, etc. Can be manipulated further like changing colors          
        print res['quoteErrors']

# Create your views here.
