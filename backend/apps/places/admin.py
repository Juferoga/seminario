from django.contrib import admin
from .models import Place

class PlaceAdmin(admin.ModelAdmin):
  list_display = (
    'pk_id', 't_name', 't_description','n_type', 't_observation', 
    'd_created_at', 'd_updated_at', 'n_price', 'b_status'
    )
  list_filter = ('n_type', 'd_created_at', 'd_updated_at', 'b_status')
  search_fields = ('pk_id', 'n_type', 'description')
  readonly_fields = ('d_created_at', 'd_updated_at')
  ordering = ('-d_created_at',)

  fieldsets = (
    ('Información Básica', {
      'fields': (
        't_name', 't_description', 
        'n_type', 't_observation', 'n_price',
      )
    }),
    ('Fechas', {
      'fields': ('d_created_at', 'd_updated_at')
    }),
  )

admin.site.register(Place, PlaceAdmin)
