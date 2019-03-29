from django.contrib import admin

# Register your models here.

from .models import Phone
# Register your models here.


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass
