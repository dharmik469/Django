from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from category.models import *
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        encpwd = make_password(password)

        if Register.objects.filter(username = username).exists():
            messages.error(request, 'username already exists!')
            return redirect('/register')

        if first_name and last_name and username and password:
            user = Register.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = encpwd
            )

            user.save()
            messages.success(request, 'You are register successfully!!')
            return redirect('/dd')
        else:
            context = {'register' : 'all fields are required'}
            return render(request, 'register.html', context)

    return render(request, 'register.html')

def dd(request):
    if request.session.get('name'):
        return redirect('/category-show')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =  Register.objects.filter(username = username).first()

        if user is not None:
            if check_password(password, user.password):
                messages.success(request, 'You are login successfully!')
                request.session['name'] = user.username
                request.session['password']=user.password
                response = HttpResponse('set cookies')
                response = redirect('/category-show')
                response.set_cookie('name', user.username, max_age=1)
                return response
        else:
            messages.error(request, 'Invalid username or password!!')
            return redirect('/dd')

    return render(request, 'dd.html')

def success(request):
    return render(request, 'success.html')

def category_show(request):
    queryset = Register.objects.all()
    context = {'register' : queryset}
    if request.session.get('name'):
    # name = request.COOKIES.get('name')  
        return render(request, 'category_show.html', context)
    else:
        return redirect('/dd/')

def edit(request, id):
    queryset = Register.objects.get(id=id)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        queryset.first_name = first_name
        queryset.last_name = last_name

        queryset.save()
        return redirect('/category-show/')

    context = {'register' : queryset}

    return render(request, 'category_edit.html', context)

def delete(request, id):
    queryset = Register.objects.get(id=id)
    queryset.delete()
    return redirect('/category-show/')


def mail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')

        if Email.objects.filter(email = email).exists():
            messages.error(request, 'Email is already exists!')
            return redirect('/mail')

        if email and contact and message:
            user = Email.objects.create(
                email = email,
                contact = contact,
                message = message
            )

        subject = f'Form submision from {user.email}'
        message = f'Email: {user.email} \n Contact: {user.contact} \n Message: {user.message}'
        admin_email = 'admin_email@example.com'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])

        user.save()
        return redirect('/success')
    return render(request, 'mail.html')


def logout(request):
    request.session.flush()
    return render(request, 'dd.html')