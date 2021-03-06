from __future__ import unicode_literals
from django.db import models

import re, bcrypt
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9,+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def regValidator(self, postData):
        errors = {}
        if  EMAIL_REGEX.match(postData['email']) == None:
            errors['email'] = "Invalid Email"
        elif User.objects.filter(email = postData['email']):
            errors['email'] ="Account exists"

        if len(postData['first_name']) < 3 or not postData['first_name'].isalpha():
            errors['first_name'] = "First Name must be atleast 3 char long and alphas"

        if len(postData['last_name']) < 3 or not postData['last_name'].isalpha():
            errors['last_name'] = "Last Name must be atleast 3 char long and alphas"



        if len(postData['password']) < 8:
            errors['password'] = "Password must be atleast 8 char"

        elif postData['password'] != postData['pwconf']:
            errors['pwconf'] = "Passwords doesn't match"
        print(errors)
        return errors

    def loginValidator(self, postData):
        user = User.objects.filter(email = postData['login_email'])
        errors = {}
        if not user:
            errors['login_email'] = "Please enter a valid email"
        if user and not bcrypt.checkpw(postData['login_password'].encode('utf8'), user[0].password.encode('utf8')):
            errors['login_password'] = " Incorrect Password"
        return errors



class User(models.Model):

	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()


class Quote(models.Model):
    author = models.CharField(max_length = 255)
    content = models.TextField()
    uploader = models.ForeignKey(User, related_name = "uploaded_by")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    liked_user = models.ManyToManyField(User, related_name = "liked_quotes")