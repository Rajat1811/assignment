from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.site_header = 'Rajat Administration'
admin.site.site_title = 'Rajat Administration'
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name','phone_number', 'email', 'address']
