from django.contrib import admin

from petstagram.acounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInLineAdmin,)
    list_display = ('first_name', 'last_name')
