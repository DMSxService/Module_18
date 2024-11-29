from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    text = 1
    name = 'tom'
    list = [1.1,2.2,3.3]
    len_list = len(list)
    context = {'text': text,
               'name': name,
               'list': list,
               'len_list': len_list,
    }
    return render(request, 'index.html', context)


# class index2(TemplateView):
#     template_name = 'index2.html'

