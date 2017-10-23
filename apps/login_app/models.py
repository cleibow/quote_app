# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
import bcrypt
import re

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+/.[a-zA-Z]+$')

from django.db import models
class UserManager(models.Manager):
    # Manager is a default attribute of models
    def login(self, postData):
        email = postData['email'].lower()
        password = postData['password']
        users = User.objects.filter(email = email)
        if len(users):
            user = users[0]
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return user
        return False

    def userIsValid(self, postData):
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        password = postData['password']
        cpassword = postData['cpassword']
        errors = []
        
        if len(first_name) < 2 or len(last_name) < 2 or len(email) < 2:
            errors.append('Fields must be filled out')
        if len(password) < 8 or len(cpassword) < 8:
            errors.append('Passwords must be 8 or more characters')
        else:
            if password != cpassword:
                errors.append('Passwords must match')
        return {'status': len(errors) == 0, 'errors':errors}

    def createUser(self, postData):
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email'].lower()
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()) #collect the password
        return self.create(first_name = first_name, last_name = last_name, email = email, password = password)

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    cpassword = models.CharField(max_length = 255)
    objects = UserManager()


    def __str__(self):
        return "First_name: {}, last_name: {}, email: {}, password: {}, cpassword: {}".format(self.first_name, self.last_name, self.email, self.password, self.cpassword)


# Create your models here.
