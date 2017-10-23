# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from ..login_app import views
from django.contrib import messages

from django.db import models
class QuoteManager(models.Manager):
    def quoteVal(self,post):
        quoteErrors = []
        print post['author']
        author = post['author']
        content = post['content']
        if len(author) < 2: 
            quoteErrors.append('Author name must be greater than 2 characters.')
        elif len(author) > 255 :
            quoteErrors.append('Author name has too many characters')
        elif len(content) < 2:
            quoteErrors.append('Content must be filled out')
        elif len(content) > 255: 
            quoteErrors.append('Content has too many characters')
        return {'status': len(quoteErrors) == 0, 'quoteErrors':quoteErrors}

    def displayQuote(self):
        return self.get(id = user_id)

    def newQuote(self,post):
        author = post['author']
        content = post['content']
        test_id = int(post['user_id'])
        print test_id
        ##### WHY CANT I GET THE USER ID TO WORK?? :(
        user_id = 2
        
        #need to know how to give it correct id
        #get user_id from login app render
        user = User.objects.get(id = user_id)
        return self.create(author = author, content = content, user = user)
class Quotes(models.Model):
    author = models.CharField(max_length = 255)
    content = models.CharField(max_length = 255)
    user = models.ForeignKey(User, related_name = "quotes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()

    def __str__(self):
        return "Author: {}, Content: {}, User: {}".format(self.author, self.content, self.user)
# Create your models here.
