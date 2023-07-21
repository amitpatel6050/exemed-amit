from import_export import resources

from django.contrib import admin

from myapp.resources import Contact_usResource 

from myapp.resources import Employee_regResource 
from .models import Contact_us
from .models import Employee_reg
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class Contact_usAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Contact_usResource

class Employee_regAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Employee_regResource


# class user_rgpAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     resource_class = User_rgpResource

# class logAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     resource_class = logResource
  

# admin.site.register(User_rgp , user_rgpAdmin)
admin.site.register(Contact_us , Contact_usAdmin)
admin.site.register(Employee_reg , Employee_regAdmin)

