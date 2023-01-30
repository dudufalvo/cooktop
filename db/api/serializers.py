from rest_framework import serializers
from db.models import DietaryRestriction, Ingredient, Recipe

class DietaryRestrictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryRestriction
        fields = ('dietary_restriction_id', 'name', 'description')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('ingredient_id', 'name', 'quantity')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('recipe_id', 'name', 'description', 'ingredients', 'image', 'dietary_restrictions')

# Path: db\api\views.py