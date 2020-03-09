from django.contrib.admin import ModelAdmin, register
from .models import identificacion


@register(identificacion)
class IdentificacionAdmin(ModelAdmin):
    list_display = ('nombre', 'descripcion')
    icon_name = 'assignment_ind'







