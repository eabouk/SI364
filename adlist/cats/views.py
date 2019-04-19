from cats.models import Cat, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from cats.forms import CreateForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
# Create your views here.
from cats.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from cats.util import CatListView, CatDetailView, CatCreateView, CatUpdateView, CatDeleteView


class CatListView(CatListView):
    model = Cat
    template_name = "cat_list.html"

class CatDetailView(CatDetailView):
    model = Cat
    template_name = "cat_detail.html"
    def get(self, request, pk) :
        cat = Cat.objects.get(id=pk)
        comments = Comment.objects.filter(cat=cat).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'cat' : cat, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class CatCreateView(CatCreateView):
    model = Cat
    fields = ['name','foods', 'weight']
    template_name = "cat_form.html"

class CatUpdateView(CatUpdateView):
    model = Cat
    fields = ['name', 'foods', 'weight']
    template_name = "cat_form.html"

class CatDeleteView(CatDeleteView):
    model = Cat
    template_name = "cat_delete.html"
    
class CatFormView(LoginRequiredMixin, View):
    template = 'cat_form.html'
    success_url = reverse_lazy('cats')
    def get(self, request, pk=None) :
        if not pk : 
            form = CreateForm()
        else: 
            pic = get_object_or_404(Cat, id=pk, owner=self.request.user)
            form = CreateForm(instance=pic)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            pic = get_object_or_404(Cat, id=pk, owner=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Adjust the model owner before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)
    
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Cat, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, cat=f)
        comment.save()
        return redirect(reverse_lazy('cat_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "cats_comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        Cat = self.object.cat
        return reverse_lazy('cat_detail', args=[Cat.id])

