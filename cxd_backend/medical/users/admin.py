from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from medical.users.forms import UserChangeForm, UserCreationForm
from medical.users.models import UserProfile

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + tuple(
        auth_admin.UserAdmin.fieldsets
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    model = UserProfile
