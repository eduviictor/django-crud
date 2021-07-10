from django.contrib import admin
from users.models import User

class Users(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'lastName', 'profileImageUrl', 'bio', 'email', 'gender')
    list_display_links = ('id', 'username', 'name', 'lastName', 'profileImageUrl', 'bio', 'email', 'gender')
    search_fields = ('username', 'email')

admin.site.register(User, Users)