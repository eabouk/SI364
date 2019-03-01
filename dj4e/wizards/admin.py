from django.contrib import admin

# Register your models here.
from wizards.models import House, Wizard

admin.site.register(House)
admin.site.register(Wizard)