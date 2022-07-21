from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserAgentChangeForm, UserAgentForm

PdfAdmin = get_user_model()


class UserAgentAdmin(UserAdmin):
    add_form = UserAgentForm

    form = UserAgentChangeForm
    list_of_display = ['email', 'business_name', 'logo']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('business_name', 'logo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'business_name', 'logo')}),
    )


admin.site.register(PdfAdmin, UserAgentAdmin)
