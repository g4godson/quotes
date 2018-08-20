from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):

    return render(request, 'index.html')

def register(request):
    # if User.objects.filter(email = request.POST['email']):
    #     return redirect('/')
    msgs = User.objects.regValidator(request.POST)
    if msgs:
        print(msgs)
        for key,values in msgs.items():
            print("value : ",values,"key",key)
            messages.error(request, values, extra_tags = key)



        return redirect('/')
    else :
        password = request.POST['password']
        hashedpw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashedpw)
        request.session['logged_in'] = user.id
        request.session['status'] = "Registered"
        return redirect('/success')

def login(request):
    msgs = User.objects.loginValidator(request.POST)
    if msgs:
        for key,values in msgs.items():
            print("value : ",values,"key",key)
            messages.error(request, values, extra_tags = key)

        return redirect('/')

    else:
        users = User.objects.filter(email = request.POST['login_email'])
        request.session['logged_in'] = users[0].id
        request.session['status'] = "logged in"
        return redirect('/success')




def success(request):
    return redirect('/home')

def logout(request):
    request.session.clear()
    return redirect('/')


def home(request):
    if not request.session['logged_in']:
        return redirect('/')
    quotes = Quote.objects.order_by('-created_at')

    user = User.objects.get(id = request.session['logged_in'])
    return render(request,"home.html", {'quotes' : quotes, 'user': user.first_name},  )

def add(request):
    if not request.session['logged_in']:
        return redirect('/')
    print('inside add')
    print(request.POST['author'], request.POST['content'])
    user = User.objects.get(id = int(request.session['logged_in']))
    print("user = ",user)

    new = Quote.objects.create(author = request.POST['author'], content = request.POST['content'], uploader = user)

    print("!!!!created", new.uploader,"@@@")
    return redirect('/home')

def like(request,id):
    quote = Quote.objects.get(id = id)
    user = User.objects.get(id = int(request.session['logged_in']))
    quote.liked_user.add(user)
    return redirect('/home')

def delete(request,id):
    obj = Quote.objects.get(id = id)
    obj.delete()
    return redirect('/home')

def edit(request,id):
    return render(request,'edit.html',{'obj' : User.objects.get(id=id)})

def update(request,id):
    obj = User.objects.get(id=id)
    if request.POST['first_name']:
        obj.first_name = request.POST['first_name']

    if request.POST['last_name']:
        obj.last_name= request.POST['last_name']

    if request.POST['email']:
        obj.email= request.POST['email']

    obj.save()
    return redirect('/home')

def show(request, id):
    objs = Quote.objects.filter(id = id)
    user = objs[0].uploader.first_name
    #user = User.objects.get(id = int(user))
    print(user)
    return render(request, 'show.html', {'objs': objs, 'posted_user' : user})