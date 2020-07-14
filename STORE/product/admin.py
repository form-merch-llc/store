from django.contrib import admin

from .models import (
    Attribute,
    Image,
    Product,
    Type,
    Variant,
    Value,
)


class AttributeInline(admin.StackedInline):
    model = Attribute


class ImageInline(admin.StackedInline):
    model = Image


class VariantInline(admin.StackedInline):
    model = Variant


class ValueInline(admin.StackedInline):
    model = Value


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    inlines = [ValueInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["pk", "alt"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    inlines = [VariantInline]


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    inlines = [ImageInline]


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
