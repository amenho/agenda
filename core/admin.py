from django.contrib import admin
from core.models import Eventos


# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo',)


admin.site.register(Eventos, EventoAdmin)
