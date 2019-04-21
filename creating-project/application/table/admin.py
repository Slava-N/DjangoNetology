from django.contrib import admin

# Register your models here.
from table.models import Table_setup, Path_to_file


admin.site.register(Table_setup)
admin.site.register(Path_to_file)