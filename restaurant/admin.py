from django.contrib import admin
from restaurant.models import Menu
class MenuAdmin(admin.ModelAdmin):
  pass

admin.site.register(Menu, MenuAdmin)
# Register your models here.
