from django.contrib import admin

from home.models import TodoUser


class TodoUserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "date_joined", "last_login", "is_superuser")


admin.site.register(TodoUser, TodoUserAdmin)
