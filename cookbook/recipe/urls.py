from django.urls import path

from .views import add_product_to_recipe, cook_recipe, show_recipe

app_name = "recipe"

urlpatterns = [
    path("add_product_to_recipe/", add_product_to_recipe, name="add_product_to_recipe"),
    path("cook_recipe/", cook_recipe, name="cook_recipe"),
    path("show_recipe/", show_recipe, name="show_recipe"),
]
