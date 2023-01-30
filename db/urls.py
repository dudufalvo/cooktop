from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from db.api import viewsets

app_name='db'
urlpatterns = [
    path('', viewsets.get_routes),
    # path('users/', viewsets.UserList.as_view()),
    # path('users/<int:pk>/', viewsets.UserDetail.as_view()),
    path('dietaryrestrictions/', viewsets.DietaryRestrictionList.as_view()),
    path('dietaryrestrictions/<int:pk>/', viewsets.DietaryRestrictionDetail.as_view()),
    path('ingredients/', viewsets.IngredientList.as_view()),
    path('ingredients/<int:pk>/', viewsets.IngredientDetail.as_view()),
    path('recipes/', viewsets.RecipeList.as_view()),
    path('recipes/<int:pk>/', viewsets.RecipeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)