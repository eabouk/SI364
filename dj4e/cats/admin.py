from django.contrib import admin

# Register your models here.
from cats.models import Breed, Cats

admin.site.register(Breed)
admin.site.register(Cats)