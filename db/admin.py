from django.contrib import admin
from .models import DietaryRestriction, Ingredient, Recipe

# Register your models here.

# admin.site.register(User)
admin.site.register(DietaryRestriction)
admin.site.register(Ingredient)
admin.site.register(Recipe)