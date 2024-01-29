from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

from .models import RecipeItem, Product, Recipe


# Create your views here.


def add_product_to_recipe(request: HttpRequest):
    try:
        recipe_id = int(request.GET.get("recipe_id"))
        product_id = int(request.GET.get("product_id"))
        weight = int(request.GET.get("weight"))
    except TypeError:
        return HttpResponseNotFound("Параметры переданы некорректно")
    recipe_item, create = RecipeItem.objects.get_or_create(
        recipe_id=recipe_id, product_id=product_id
    )
    recipe_item.product_weight = weight
    recipe_item.save()
    if create:
        return HttpResponse("Продукт добавлен", status=200)
    return HttpResponse("Продукт изменен", status=200)


def cook_recipe(request: HttpRequest):
    try:
        recipe_id = int(request.GET.get("recipe_id"))
    except TypeError:
        return HttpResponseNotFound("Параметры переданы некорректно")
    items = (
        RecipeItem.objects.all().filter(recipe_id=recipe_id).select_related("product")
    )
    for item in items:
        product = item.product
        product.count_cook += 1
        product.save()
    return HttpResponse("Рецепт приготовлен", status=200)


def show_recipe(request: HttpRequest):
    try:
        product_id = int(request.GET.get("product_id"))
    except TypeError:
        return HttpResponseNotFound("Параметры переданы некорректно")
    exc = (
        item.recipe_id
        for item in RecipeItem.objects.filter(product_id=product_id).filter(
            product_weight__gte=10
        )
    )

    recipes = Recipe.objects.exclude(id__in=exc)
    context = {"recipes": recipes}
    return render(request, "recipe/show.html", context=context)
