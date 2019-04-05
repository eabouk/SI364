from ads.models import Ad

from django.views import View
from django.views import generic
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from ads.forms import CreateForm

# Create your views here.

from ads.util import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView


class AdListView(AdListView):
    model = Ad
    template_name = "ad_list.html"

class AdDetailView(AdDetailView):
    model = Ad
    template_name = "ad_detail.html"

#class AdCreateView(AdCreateView):
#    model = Ad
#    fields = ['title','price', 'text']
#    template_name = "ad_form.html"
#
#class AdUpdateView(AdUpdateView):
#    model = Ad
#    fields = ['title', 'price', 'text']
#    template_name = "ad_form.html"

class AdDeleteView(AdDeleteView):
    model = Ad
    template_name = "ad_delete.html"
    
class AdFormView(LoginRequiredMixin, View):
    template = 'ad_form.html'
    success_url = reverse_lazy('ads')
    def get(self, request, pk=None) :
        if not pk : 
            form = CreateForm()
        else: 
            pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
            form = CreateForm(instance=pic)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Adjust the model owner before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

def stream_file(request, pk) :
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response