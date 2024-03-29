from django.contrib import admin
from .models import User, Record
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
# Register your models here.

admin.site.register(Record)

@admin.register(User)
class AdminUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'full_name', 'is_staff')
    search_fields = ('username', 'full_name', 'email')
    filter_horizontal = ('user_permissions',)
