from django.contrib import admin
from amer.models import Character

from  .forms import CharacterForm

class AdminCharacter(admin.ModelAdmin):
    list_display = ["__str__","power","speed","capacity_width","capacity_height"] ## co chcesz widziec w utworzonym modelu w  adminie
    form = CharacterForm
    #po dodaniu formatki beda widoczne tylko fields z klasy CharacterForm
    class Meta:
        model = Character
# Register your models here.
admin.site.register(Character, AdminCharacter)


