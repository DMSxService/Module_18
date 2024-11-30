from django.shortcuts import render
from django.http import HttpResponse


def sign_up_by_django(request):
    if request.method == 'POST':
        username = request.POST.get('username', 'user')
        return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_html(request):
    username = request.GET.get('username', 'Guest')
    password = request.GET.get('password', '')
    age = request.GET.get('age', '0')
    return HttpResponse(f'Hello, {username} {age}!')
