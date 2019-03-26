from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.utils.functional import SimpleLazyObject
from django.utils.ipv6 import is_valid_ipv6_address
from django.utils.translation import gettext_lazy as _, ngettext_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your models here.

class Ad(models.Model) :
    title = models.CharField(
            max_length=200,
#            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
#    ) 
        #Not sure why this validator keeps saying "MinLengthValidator not defined"
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title
    
    

