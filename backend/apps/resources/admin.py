from django.contrib import admin
from .models import Resource

class ResourceAdmin(admin.ModelAdmin):
    list_display = (
          'pk_id', 't_name', 't_description',
          'd_created_at', 'd_updated_at', 
          'n_price', 'b_status'
        )
    list_filter = ( 'd_created_at', 'd_updated_at', 'b_status')
    search_fields = ('pk_id',  'description')
    readonly_fields = ('d_created_at', 'd_updated_at')
    ordering = ('-d_created_at',)

    fieldsets = (
        ('Información Básica', {
            'fields': (
              't_name', 
              't_description', 
              'n_price',
              'fk_reservation'
            )
        }),
        ('Fechas', {
            'fields': ('d_created_at', 'd_updated_at')
        }),
    )

admin.site.register(Resource, ResourceAdmin)