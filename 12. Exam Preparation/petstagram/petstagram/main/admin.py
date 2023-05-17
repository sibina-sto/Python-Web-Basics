from django.contrib import admin

from petstagram.main.models import Pet, PetsPhoto


class PetInLineAdmin(admin.StackedInline):
    model = Pet





@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetsPhoto)
class PetsPhotoAdmin(admin.ModelAdmin):
    pass
