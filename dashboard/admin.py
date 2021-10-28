from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import datamodel
# Register your models here.
class datatableAdmin(ImportExportModelAdmin):
    pass

admin.site.register(datamodel,datatableAdmin)