from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class UserProfileInLine(admin.StackedInline):
    model = UserProfile


# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         (_("Personal info"), {
#             "fields": ("first_name", "last_name", "email", "date_of_birth", "title")
#         }),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "password1", "password2"),
#             },
#         ),
#     )
#     inlines = [UserProfileInLine]

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username', 'date_of_birth',
                    'title', 'is_staff', 'is_superuser')
    list_filter = ('is_active',)


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(CustomUser)
