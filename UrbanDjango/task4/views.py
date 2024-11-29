from django.shortcuts import render
from django.views.generic import TemplateView


class ClassPlatform(TemplateView):
    head = 'Главная страница'
    cont = ''
    template_name = 'fourth_task/platform.html'
    extra_context = {'head': head, 'cont': cont}


def func_games(request):
    head = 'Игры'
    button1 = "Купить"
    context = {
        'head': head,
        'games': ['AtomicHeart', 'Cyberpunk2077', 'PayDay 2'],
        'b1': button1
    }
    return render(request, 'fourth_task/games.html', context)


class ClassCart(TemplateView):
    head = 'Корзина'
    cont = 'Извините, ваша корзина пуста'
    template_name = 'fourth_task/cart.html'
    extra_context = {'head': head, 'cont': cont}
