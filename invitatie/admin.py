from django.contrib import admin
from .models import Confirm
from import_export.admin import ExportActionMixin

# Register your models here.

# Register your models here.
class ConfirmAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'people', 'confirm')

admin.site.register(Confirm, ConfirmAdmin)
