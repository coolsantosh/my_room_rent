from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id','room_type', 'size','rent_price',
                    'is_available', 'district']

    # list_filter = ['room_type', 'status', 'is_available']
    # search_fields = ['room_number', 'street_address', 'city', 'district']

admin.site.register(Room, RoomAdmin)
