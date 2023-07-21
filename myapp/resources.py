
from import_export import resources
from .models import *

class Contact_usResource(resources.ModelResource):
    class Meta:
        model = Contact_us

class Employee_regResource(resources.ModelResource):
    class Meta:
        model = Employee_reg

# class User_rgpResource(resources.ModelResource):
#     class Meta:
#         model = User_rgp

