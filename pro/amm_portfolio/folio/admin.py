from django.contrib import admin

# Register your models here.

from .models import dbportfolio
# Register your models here.
class dbportfolioAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

    
admin.site.register(dbportfolio, dbportfolioAdmin)