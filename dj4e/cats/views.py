from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

from autos.models import Cats, Breed
from autos.forms import MakeForm

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        bc = breed.objects.all().count();
        cats = cats.objects.all();

        ctx = { 'breed_count': bc, 'cats_list': cats };
        return render(request, 'cats/cats_list.html', ctx)

class BreedView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = breeds.objects.all();
        ctx = { 'breed_list': ml };
        return render(request, 'cats/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats')
    def get(self, request) :
        form = MakeForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = MakeForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        breed = form.save()
        return redirect(self.success_url)

class BreedUpdate(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('cats')
    template = 'cats/breed_form.html'
    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        form = BreedForm(instance=make)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        form = BreedForm(request.POST, instance = make)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Make
    success_url = reverse_lazy('cats')
    template = 'catss/make_confirm_delete.html'

    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        form = BreedForm(instance=breed)
        ctx = { 'breed': breed }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk) 
        make.delete()
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
    
    