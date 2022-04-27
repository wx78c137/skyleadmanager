from django.contrib import admin
from .models import Lead, Task


# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'note', 'status']


class TaskAdmin(admin.ModelAdmin):
    def queryset(self, request):
        queryset = super(TaskAdmin, self).queryset(request)
        queryset = queryset.filter(staff=request.user)
        return queryset
    list_display = ['date', 'staff', 'description', 'status']
    list_filter = ['date']
    search_fields = ['date']


admin.site.register(Lead, LeadAdmin)
admin.site.register(Task, TaskAdmin)
