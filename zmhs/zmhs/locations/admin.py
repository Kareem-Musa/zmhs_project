from django.contrib import admin
from .models import State , Locality , Unity , City , District

class StateAdmin(admin.ModelAdmin):
    list_display = ('name','created','updated','slug')
    search_fields = ('name',)
    ordering = ('-created',)

class LocalityAdmin(admin.ModelAdmin):
    list_display = ('name','created','updated','slug')
    search_fields = ('name',)
    ordering = ('-created',)

class UnityAdmin(admin.ModelAdmin):
    list_display = ('name','created','updated','slug')
    search_fields = ('name',)
    ordering = ('-created',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','created','updated','slug')
    search_fields = ('name',)
    ordering = ('-created',)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name','created','updated','slug')
    search_fields = ('name',)
    ordering = ('-created',)

admin.site.register(State,StateAdmin)
admin.site.register(Locality,StateAdmin)
admin.site.register(Unity,StateAdmin)
admin.site.register(City,StateAdmin)
admin.site.register(District,StateAdmin)
