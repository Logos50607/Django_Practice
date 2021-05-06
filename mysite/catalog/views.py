from django.shortcuts import render
from django.views import generic
from .models import Questionnaire
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context=context)

class AnswerListView(generic.ListView):
    model = Questionnaire

class DataCreate(CreateView):
    model = Questionnaire
    fields = ['userName', 'gender', 'favoriteCity', 'reason']
    success_url = reverse_lazy('answers')

class DataUpdate(UpdateView):
    model = Questionnaire
    fields = '__all__'