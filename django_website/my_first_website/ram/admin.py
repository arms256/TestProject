from django.contrib import admin
from . models import Pokemon
from .models import UserInfo
# Register your models here.


class RamPokemonAdmin(admin.ModelAdmin):
    list_display = ('Pokemon_Name','POWER','value')


admin.site.register(Pokemon,RamPokemonAdmin)
admin.site.register( UserInfo )