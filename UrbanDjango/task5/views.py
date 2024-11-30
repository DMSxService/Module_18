from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['Миша', 'Петя', 'Таня', 'Степа', 'Андрей']
info = {}


def sign_up_by_django(request):
    global info
    error = ""
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            greeting = f'Приветствуем,{username} !'
            if username in users:
                error = 'Пользователь уже существует'
                greeting = ''
            if password != repeat_password:
                error = 'Пароли не совпадают'
                greeting = ''
            if int(age) < 18:
                error = 'Вы должны быть старше 18'
                greeting = ''
            info = {'form': form, 'greeting': greeting, 'error': error,
                    'username': username, 'password': password,
                    'repeat_password': repeat_password, 'age': age}
    else:
        form = UserRegister()

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    global info
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        greeting = f'Приветствуем,{username} !'
        if username in users:
            error = 'Пользователь уже существует'
            greeting = ''
        if password != repeat_password:
            error = 'Пароли не совпадают'
            greeting = ''
        if int(age) < 18:
            error = 'Вы должны быть старше 18'
            greeting = ''
        info = {'greeting': greeting, 'error': error,
                'username': username, 'password': password,
                'repeat_password': repeat_password, 'age': age}
        return render(request, 'fifth_task/registration_page.html', info)
    return render(request, 'fifth_task/registration_page.html')
