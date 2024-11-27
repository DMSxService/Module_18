from django.shortcuts import render
from django.views.generic import TemplateView


class ClassPlatform(TemplateView):
    template_name = 'third_task/platform.html'


def func_games(request):
    head = 'Игры'
    game1 = 'Atomic Heart'
    game2 = 'Cyberpunk 2077'
    game3 = 'PayDay 2'
    button1 = "Купить"
    button2 = 'Вернуться обратно'
    context = {
        'head': head,
        'g1': game1, 'g2': game2, 'g3': game3,
        'b1': button1, 'b2': button2
    }
    return render(request, 'third_task/games.html', context)


class ClassCart(TemplateView):
    head = 'Извините, ваша корзина пуста'
    button2 = 'Вернуться обратно'
    template_name = 'third_task/cart.html'
    extra_context = {'h': head, 'b2': button2}
