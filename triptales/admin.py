"""Admin configuration for the triptales app."""
from django.contrib import admin
from triptales.models import *

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class locationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'likes')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio',)

admin.site.register(Country, CountryAdmin)
admin.site.register(Location, locationAdmin)
admin.site.register(VacationPost, postAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile, UserProfileAdmin)