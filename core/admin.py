from django.contrib import admin
from .models import Lang, Audio, Rating

# Register your models here.
admin.site.register(Lang)
admin.site.register(Audio)
admin.site.register(Rating)
