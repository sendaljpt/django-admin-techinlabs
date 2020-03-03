from django.contrib import admin

from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('color', 'category__name')
    readonly_fields = ('sku',)

    list_display = ('name', 'color', 'stock', 'get_category',)
    search_fields = ['name', 'color',]

    autocomplete_fields = ['category']

    fieldsets = [
        ('Category', {'fields': ['category']}),
        ('Detail Product', {'fields': ['name', 'color', 'stock', ]}),
        ('SKU Number', {'fields': ['sku', ]}),
        
    ]

    def get_category(self, obj):
        return obj.category.name
    get_category.short_description = 'Category'
    get_category.admin_order_field = 'category__name'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
