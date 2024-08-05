
from django.contrib import admin
from .models import Contact, Concert,Booking

class ConcertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'venue', 'location', 'trailer_url', 'timings', 'artists')

admin.site.register(Contact)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Booking)




