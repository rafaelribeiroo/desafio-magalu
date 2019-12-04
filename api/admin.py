from django.contrib import admin
from .models import Product, Client


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_display_links = ['title']
    list_editable = ['price']
    list_filter = ['brand']
    search_fields = ['title']
    save_on_top = True

    class Meta:
        model = Product


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['email']
    save_on_top = True

    class Meta:
        model = Client
