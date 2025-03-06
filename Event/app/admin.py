from django.contrib import admin
from .models import Band,Event,BandEvent

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True;

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return


admin.site.register(Band)
admin.site.register(Event)
admin.site.register(BandEvent)
