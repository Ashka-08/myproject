from django.contrib import admin
from hw3_app.models import User, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(prod_quant=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'price', 'prod_quant']
    ordering = ['price', '-prod_quant']
    list_filter = ['reg_date', 'price', 'prod_quant']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]
    """Отдельный продукт."""
    readonly_fields = ['reg_date']
    fieldsets = [ 
        (
            None,
            {
            'classes': ['wide'],
            'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
            'classes': ['collapse'],
            'description': 'Подробное описание товара',
            'fields': ['description', 'img'],
            },
        ),
        (
            'Бухгалтерия',
            {
            'fields': ['price', 'prod_quant'],
            }
        ),
        (
            'Прочее',
            {
            'description': 'Дата добавления',
            'fields': ['reg_date'],
            }
        ),
    ]


class UserAdmin(admin.ModelAdmin):
    """Список пользователей."""
    list_display = ['name', 'reg_date']
    ordering = ['reg_date']
    list_filter = ['reg_date']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя (name)'
    """Отдельный пользователь."""
    fields = ['name', 'email', 'phone', 'address']
    readonly_fields = ['reg_date']


class OrderAdmin(admin.ModelAdmin):
    """Список заказов."""
    list_display = ['pk', 'customer', 'total_price', 'date_ordered']
    ordering = ['-date_ordered']
    list_filter = ['customer', 'total_price', 'date_ordered']
    """Отдельный заказ."""
    fields = ['customer', 'total_price', 'products']
    readonly_fields = ['date_ordered']


admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)