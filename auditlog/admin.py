from django.contrib import admin
from .models import LogEntry
from .mixins import LogEntryAdminMixin
from .filters import ResourceTypeFilter
from django.contrib import messages


class LogEntryAdmin(admin.ModelAdmin, LogEntryAdminMixin):
    list_display = ['created', 'resource_url', 'action', 'msg_short', 'user_url']
    search_fields = ['timestamp', 'object_repr', 'changes', 'actor__first_name', 'actor__last_name']
    list_filter = ['action', ResourceTypeFilter]
    # readonly_fields = ['created', 'resource_url', 'action', 'user_url', 'msg']
    fieldsets = [
        (None, {'fields': ['created', 'user_url', 'resource_url']}),
        ('Changes', {'fields': ['action', 'msg']}),
    ]

    def save_model(self, request, obj, form, change):
        try:

            messages.info["Nao pode salvar"]
            # requisitante = Requisitante.objects.get(id_user=request.user.pk)
            # obj.solicitante = requisitante
            # obj.chave_anonimo = requisitante.chave_identificacao
            # obj.longitude = request.POST.get('codigo_longitude') or None
            # obj.lagitude = request.POST.get('codigo_latitude') or None
            obj.save()
        except:
            pass


admin.site.register(LogEntry, LogEntryAdmin)
