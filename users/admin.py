from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'created_at', 'updated_at', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
