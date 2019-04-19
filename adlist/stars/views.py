from stars.models import Star, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from stars.forms import CreateForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
# Create your views here.
from stars.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from stars.util import StarListView, StarDetailView, StarCreateView, StarUpdateView, StarDeleteView


class StarListView(StarListView):
    model = Star
    template_name = "star_list.html"

class StarDetailView(StarDetailView):
    model = Star
    template_name = "star_detail.html"
    def get(self, request, pk) :
        star = Star.objects.get(id=pk)
        comments = Comment.objects.filter(star=star).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'star' : star, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class StarCreateView(StarCreateView):
    model = Star
    fields = ['name','foods', 'weight']
    template_name = "star_form.html"

class StarUpdateView(StarUpdateView):
    model = Star
    fields = ['name', 'foods', 'weight']
    template_name = "star_form.html"

class StarDeleteView(StarDeleteView):
    model = Star
    template_name = "star_delete.html"
    
class StarFormView(LoginRequiredMixin, View):
    template = 'star_form.html'
    success_url = reverse_lazy('stars')
    def get(self, request, pk=None) :
        if not pk : 
            form = CreateForm()
        else: 
            pic = get_object_or_404(Star, id=pk, owner=self.request.user)
            form = CreateForm(instance=pic)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            pic = get_object_or_404(Star, id=pk, owner=self.request.user)
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
        f = get_object_or_404(Star, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, star=f)
        comment.save()
        return redirect(reverse_lazy('star_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "stars_comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        Star = self.object.star
        return reverse_lazy('star_detail', args=[Star.id])

