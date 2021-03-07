from django.contrib import admin
from .models import Team, Match

# Register your models here.

admin.site.register(Match)
admin.site.register(Team)