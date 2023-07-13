from django.contrib import admin

from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
    Order,
    Ticket,
)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ("title", "description")
    list_filter = ("title", "duration", "genres", "actors")


admin.site.register(Actor)
admin.site.register(CinemaHall)
admin.site.register(Genre)
admin.site.register(MovieSession)
admin.site.register(Order)
admin.site.register(Ticket)
