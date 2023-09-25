from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = (
          'pk_id', 'd_reservation', 
          'd_created_at', 'b_status'
        )
    list_filter = ('d_reservation', 'd_created_at', 'b_status')
    search_fields = ('pk_id', 'd_reservation')
    readonly_fields = ('d_created_at',)
    ordering = ('-d_created_at',)

    fieldsets = (
        ('Información Básica', {
            'fields': (
                'd_reservation', 'b_status',
                'fk_customer', 'fk_student',
                'fk_employee', 'fk_payment'
            )
        }),
        ('Fechas', {
            'fields': ('d_created_at',)
        }),
    )

admin.site.register(Reservation, ReservationAdmin)