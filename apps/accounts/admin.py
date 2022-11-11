from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from apps.accounts.models import User

from apps.accounts.forms import UserAdminCreationForm, UserAdminChangeForm


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = User

    list_display = ['username', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'is_author']
    list_filter = ['is_superuser', 'is_staff', 'is_author']
    search_fields = ['username', 'first_name', 'last_name']
    readonly_fields = ['uid', 'last_login', 'date_joined']

    fieldsets = (
        (None, {'fields': ('uid', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'is_author')}),
        ('Others', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_superuser', 'is_staff', 'is_author')}
         ),
    )


admin.site.unregister(Group)
