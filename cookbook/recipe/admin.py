from django.contrib import admin
from .models import Product, Recipe, RecipeItem


# Register your models here.
class ItemInline(admin.TabularInline):
    model = RecipeItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "id", "name", "count_recipe"


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]
    list_display = "id", "name"

