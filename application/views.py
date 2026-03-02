from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from pyexpat.errors import messages
from django.urls import reverse_lazy

from .forms import StudResultsForm
from .models import StudResults
# Create your views here.
from django.views import View


class homeview(View):
    def get(self,request):
        return render(request,'base.html')

class addresultsview(View):
    def get(self,request):
        form = StudResultsForm()
        return render(request,'addresults.html',context={'form':form})
    def post(self,request):
        form = StudResultsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
        else:
            return render(request,'addresults.html',context={'form':form})

class listresults(ListView):
    model = StudResults
    template_name = 'viewresults.html'
    context_object_name = 'student'


class updateview(UpdateView):
    model = StudResults
    template_name = 'update.html'
    form_class = StudResultsForm
    success_url = reverse_lazy('view')


class deleteview(DeleteView):
    model = StudResults
    template_name = 'delete.html'
    success_url = reverse_lazy('view')


class createview(CreateView):
    model = StudResults
    form_class = StudResultsForm
    template_name = 'addresults.html'
    success_url = reverse_lazy('view')

