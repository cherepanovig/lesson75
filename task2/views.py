from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index_func(request): # для функционального представления
    return render(request, 'func_template.html')

class index_class(TemplateView):
    template_name = 'class_template.html'


