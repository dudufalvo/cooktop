from django.utils import timezone
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


# Create your models here.
class DietaryRestriction(models.Model):
    dietary_restriction_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(_('description'), max_length=500, default='Description of the Dietary Restriction')

    def __str__(self):
        return self.name

""" class User(models.Model):
    id_token = models.CharField(primary_key=True, max_length=150, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(_('email address'), unique=True)
    image = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, default='About the User')
    dietary_restrictions = models.ManyToManyField('DietaryRestriction', blank=True)

    def __str__(self):
        return self.name
 """

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(_('description'), max_length=500, default='Description of the Recipe')
    ingredients = models.ManyToManyField('Ingredient', blank=False, related_name='recipes')
    image = models.CharField(max_length=150)
    #user = models.ForeignKey(User, on_delete=CASCADE)
    dietary_restrictions = models.ManyToManyField('DietaryRestriction', blank=True)

    def __str__(self):
        return self.name