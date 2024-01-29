from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    count_recipe = models.IntegerField(default=0)


class Recipe(models.Model):
    name = models.CharField(max_length=100)


class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_weight = models.IntegerField(default=0)