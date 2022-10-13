from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
import datetime

from django.contrib.auth.decorators import login_required

from todolist.forms import TaskForm

from .models import Task





@login_required(login_url='/todolist/login/')
def show_todolist(request): 
    username = request.user.username
    tasks_list = Task.objects.filter(user = request.user)
    context = {
    'tasks_list': tasks_list,
    'username': username
    }
    context
    return render(request, "todolist_ajax.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def create_task(request):
    form = TaskForm() 

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.create(user= request.user, title = request.POST['title'], description = request.POST['description'])
            task.save
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'create-task.html', context)

# buat fungsi show todolist in json
@login_required(login_url='/todolist/login/')
def show_todolist_in_json(request): 
    username = request.user.username
    tasks_list = Task.objects.filter(user = request.user)
    context = {
    'tasks_list': tasks_list,
    'username': username
    }
    context
    return HttpResponse(serializers.serialize("json", tasks_list), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        task = Task.objects.create(user= request.user, title = title, description=description, date=date)
        task.save
        return HttpResponse('')