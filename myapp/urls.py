from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('findia/', views.findia, name='findia'),
    path('celebration/', views.celebration, name='celebration'),
    path('career/', views.career, name='career'),
    path('brand/', views.brand, name='brand'),
    path('therapies/', views.therapies, name='therapies'),
    path('client/', views.client, name='client'),
    path('api/', views.api, name='api'),
    path('fd/', views.fd, name='fd'),
    path('reg_form/', views.reg_form, name='reg_form'),
    path('management/', views.management, name='management'),
    path('core_value/', views.core_value, name='core_value'),
    path('facilities/', views.facilities, name='facilities'),
    path('global_presence/', views.global_presence, name='global_presence'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('employee_reg/', views.employee_reg, name='employee_reg'),
   
]
