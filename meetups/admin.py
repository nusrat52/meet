from django.contrib import admin

# Register your models here.


from .models import Meetups, Location, Participants

class MeetupAdmin(admin.ModelAdmin):
    list_display=("title", "date",)
    list_filter=("title", 'date')
    prepopulated_fields={"slug":('title',)}



admin.site.register(Meetups, MeetupAdmin)

admin.site.register(Location)
admin.site.register(Participants)