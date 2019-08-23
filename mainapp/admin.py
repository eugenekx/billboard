from django.contrib import admin
from .models import Tag, Place, Org, Artist, Event

# Register your models here.

admin.site.register(Tag)

admin.site.register(Place)

admin.site.register(Org)

admin.site.register(Artist)


admin.site.register(Event)