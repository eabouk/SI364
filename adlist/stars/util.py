from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

class StarListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """

class StarDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """

class StarCreateView(LoginRequiredMixin, CreateView):
    """
    Sub-class of the CreateView to Starmatically pass the Request to the Form
    and add the owner to the saved object.
    """

    def form_valid(self, form):
        print('form_valid called')
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(StarCreateView, self).form_valid(form)

class StarUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """

    def get_queryset(self):
        print('update get_queryset called')
        """ Limit a User to only modifying their own data. """
        qs = super(StarUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)

class StarDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(StarDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)

# References

# https://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model

# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview

