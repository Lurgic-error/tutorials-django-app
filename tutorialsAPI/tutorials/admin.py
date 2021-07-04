from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tutorial, TutorialAdmin)
# Register your models here.
