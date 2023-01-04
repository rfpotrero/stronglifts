from django.contrib import admin

from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date')

    fields = ('order_number', 'date')

    list_display = ('order_number', 'date', 'order_total', 'email', 'full_name')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
