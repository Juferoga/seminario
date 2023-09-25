from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
          'pk_id', 'n_type', 
          'd_created_at', 'b_status'
        )
    list_filter = ('n_type', 'd_created_at', 'b_status')
    search_fields = ('pk_id', 'n_type')
    readonly_fields = ('d_created_at',)
    ordering = ('-d_created_at',)

    fieldsets = (
        ('Información Básica', {
            'fields': (
                'n_type', 'b_status'
            )
        }),
        ('Fechas', {
            'fields': ('d_created_at',)
        }),
    )

admin.site.register(Payment, PaymentAdmin)
