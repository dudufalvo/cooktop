from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from db.api import viewsets

app_name='db'
urlpatterns = [
    path('', viewsets.routes_list),
    path('diet_rest/', viewsets.diet_rest_list),
    path('diet_rest/<int:pk>/', viewsets.diet_rest),
    path('ingredient/', viewsets.ingredient_list),
    path('ingredient/<int:pk>/', viewsets.ingredient),
    path('recipe/', viewsets.recipe_list),
    path('recipe/<int:pk>/', viewsets.recipe),
]

urlpatterns = format_suffix_patterns(urlpatterns)