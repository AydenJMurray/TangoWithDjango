from django.contrib import admin
from Rango.models import Category, Page
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_field = {'slug':('name',)}
	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)