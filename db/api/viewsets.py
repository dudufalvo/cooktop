from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from db.api.serializers import DietaryRestrictionSerializer, IngredientSerializer, RecipeSerializer
from db.models import DietaryRestriction, Ingredient, Recipe


@api_view(['GET'])
def routes_list(request):
    if request.method == 'GET':
        routes = [
            'diet_restrictions:  http://127.0.0.1:8000/api/diet_rest/',
            'ingredients:  http://127.0.0.1:8000/api/ingredient/',
            'recipes:  http://127.0.0.1:8000/api/recipe/',
        ]
        return Response(routes)



# diet_rest/views.py
@api_view(['GET', 'POST'])
def diet_rest_list(request):
    """ list all diet restrictions, or create a new one """

    # in case of GET request
    if request.method == 'GET':
        # get all diet restrictions, serialize them, and return
        diet_restrictions = DietaryRestriction.objects.all()
        serializer = DietaryRestrictionSerializer(diet_restrictions, many=True)
        return Response(serializer.data)

    # in case of POST request
    elif request.method == 'POST':
        # serialize the data sent in the request
        serializer = DietaryRestrictionSerializer(data=request.data)
        # if the data is valid, save it to the database
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if the data is invalid, return an error message
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def diet_rest(request, id, format=None):
    """ retrieve, update, or delete a diet restriction """

    # verifies if the object exists through it's id and return a 404 ERROR if not
    try:
        diet_rest = DietaryRestriction.objects.get(pk=id)
    except DietaryRestriction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # in case of GET request
    if request.method == 'GET':
        # serialize the object and return
        serializer = DietaryRestrictionSerializer(diet_rest)
        return Response(serializer.data)

    # in case of PATCH request
    elif request.method == 'PUT':
        # updates the data of an existing dietary restriction and verifies if it still valid
        serializer = DietaryRestriction(diet_rest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # in case of DELETE request
    elif request.method == 'DELETE':
        # delete the dietary restriction and returns a no content error
        diet_rest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ingredient/views.py
@api_view(['GET', 'POST'])
def ingredient_list(request):
    """ list all ingredients, or create a new one """

    # in case of GET request
    if request.method == 'GET':
        # get all ingredients, serialize them, and return
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    # in case of POST request
    elif request.method == 'POST':
        # serialize the data sent in the request
        serializer = IngredientSerializer(data=request.data)
        # if the data is valid, save it to the database
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if the data is invalid, return an error message
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def ingredient(request, id, format=None):
    """ retrieve, update, or delete a ingredient """

    # verifies if the object exists through it's id and return a 404 ERROR if not
    try:
        ingredient = Ingredient.objects.get(pk=id)
    except Ingredient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # in case of GET request
    if request.method == 'GET':
        # serialize the object and return
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    # in case of PATCH request
    elif request.method == 'PUT':
        # updates the data of an existing ingredient and verifies if it still valid
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # in case of DELETE request
    elif request.method == 'DELETE':
        # delete the ingredient and returns a no content error
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# recipes/views.py
@api_view(['GET', 'POST'])
def recipe_list(request):
    """ list all recipes, or create a new one """

    # in case of GET request
    if request.method == 'GET':
        # get all recipes, serialize them, and return
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    # in case of POST request
    elif request.method == 'POST':
        # serialize the data sent in the request
        serializer = RecipeSerializer(data=request.data)
        # if the data is valid, save it to the database
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if the data is invalid, return an error message
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def recipe(request, id, format=None):
    """ retrieve, update, or delete a recipe """

    # verifies if the object exists through it's id and return a 404 ERROR if not
    try:
        recipe = Recipe.objects.get(pk=id)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # in case of GET request
    if request.method == 'GET':
        # serialize the object and return
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    # in case of PATCH request
    elif request.method == 'PUT':
        # updates the data of an existing recipe and verifies if it still valid
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # in case of DELETE request
    elif request.method == 'DELETE':
        # delete the recipe and returns a no content error
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)