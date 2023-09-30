from django.contrib import admin
from media import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from media import models
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """define the admin pages for user"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None, {
                'classes':('wide',),
                'fields':(
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
    )
    
admin.site.register(models.User, UserAdmin)
admin.site.register(models.TagModel)
admin.site.register(models.ImageModel)
admin.site.register(models.GalleryModel)
admin.site.register(models.News)
admin.site.register(models.Programs)
admin.site.register(models.Anouncement)
admin.site.register(models.Event)

