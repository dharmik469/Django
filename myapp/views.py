from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    peoples =[
        {'name':'Dharmik prajapati', 'age':23},
        {'name':'karan Thakor', 'age':17},
        {'name':'Sujal Desai', 'age':15},
        {'name':'Chirag Joshi', 'age':16},
        {'name':'Vinay Patel', 'age':22},
        {'name':'Akash Raval', 'age':15},    
        {'name':'Kismat desai', 'age':27},
    ]

    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

    for people in peoples:
        print(people)


    # return HttpResponse('I am Django server')
    return render(request, 'index.html', context={'peoples':peoples, 'text':text})

def about(request):

    vagetable = ["Tomato", "Cobiz", "Potato"]
    # return HttpResponse('I am Django server')
    return render(request, 'about.html', context={"vagetable":vagetable})

def services(request):
    peoples = [
        {"name":"Dharmik","age":20},
        {"name":"Gaurav","age":25},
        {"name":"Sujal","age":15},
        {"name":"Zoro","age":13},
        {"name":"Sanji","age":10},
    ]
    for people in peoples:
        print(people)

    vegetables = ["Cobbiz", "Tomato", "Potato"]

    # text = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Similique dolores asperiores id labore incidunt delectus optio sint culpa cum! Atque omnis, laboriosam a, incidunt rem sed deleniti quas fuga sunt, ullam recusandae alias? Animi neque minima tempore quibusdam voluptatibus hic dolorum, quae eius! Eos officiis assumenda dolor molestiae nesciunt. Debitis."
    # return HttpResponse('I am Django server')
    return render(request, 'Services.html', context={"peoples":peoples, "vegetables":vegetables})


def contact(request):
    peoples =[
        {'name':'Dharmik prajapati', 'age':23},
        {'name':'karan Thakor', 'age':17},
        {'name':'Sujal Desai', 'age':15},
        {'name':'Chirag Joshi', 'age':16},
        {'name':'Vinay Patel', 'age':22}, 
    ]

    for people in peoples:
        print(people)
    # return HttpResponse('I am Django server')
    return render(request, 'Contact.html', context={'peoples':peoples})

def about1(request):
    return render(request, "about1.html")

def contact1(request):
    return render(request, "contact1.html")
def login(request):
    return render(request,"login.html")


def demo(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        encpwd = make_password(password)

        if Demo.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('/demo/')
        
        if first_name and last_name and username and password:
            user = Demo.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = encpwd
            )

            user.save()
            messages.success(request, 'You are login Successfully!')
            return redirect('/get/')
        
        else:
            context = {'error': 'All fields are required!'}
            return render(request, 'demo.html', context)
    return render(request, 'demo.html')


def get(request):  
    if request.session.get('name'):
        return redirect('/about/') 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = Demo.objects.filter(username=username).first()

        if user is not None:
            if check_password(password, user.password):
                request.session['name']=user.username
                messages.success(request, 'You are login successfully!')
                return redirect('/about/')
            
            else:
                messages.error(request, 'Username or password id incorect')
                return redirect('/get/')
            
    return render(request, 'get.html')