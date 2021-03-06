from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

from cats.models import Cats, Breed
from cats.forms import BreedForm

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        bc = Breed.objects.all().count();
        cats = Cats.objects.all();

        ctx = { 'breed_count': bc, 'cats_list': cats };
        return render(request, 'cats/cats_list.html', ctx)

class BreedView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Breed.objects.all();
        ctx = { 'breeds_list': ml };
        return render(request, 'cats/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats')
    def get(self, request) :
        form = BreedForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = BreedForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        breed = form.save()
        return redirect(self.success_url)

class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats')
    template = 'cats/breed_form.html'
    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        form = BreedForm(instance=breed)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        form = BreedForm(request.POST, instance = breed)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats')
    template = 'cats/breeds_confirm_delete.html'

    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        form = BreedForm(instance=breed)
        ctx = { 'breed': breed }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        breed.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class CatsCreate(LoginRequiredMixin,CreateView):
    model = Cats
    fields = '__all__'
    success_url = reverse_lazy('cats')

class CatsUpdate(LoginRequiredMixin, UpdateView):
    model = Cats
    fields = '__all__'
    success_url = reverse_lazy('cats')

class CatsDelete(LoginRequiredMixin, DeleteView):
    model = Cats
    fields = '__all__'
    success_url = reverse_lazy('cats')
    
    