from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    # main_fields = ('brand', 'model')
    list_display = ('brand', 'model', 'review_count')
    ordering = ['-pk']
    list_filter = ('brand',)
    pass


class ReviewAdmin(admin.ModelAdmin):
    ordering = ['-pk']
    list_display = ('car',)
    list_filter = ('car',)
    search_fields = ('car', 'title')
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
