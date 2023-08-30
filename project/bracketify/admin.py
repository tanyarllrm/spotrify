from django.contrib import admin

from .models import Record


class RecordAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Song Information", {"fields": ["artist_name", "album_name", "song_name", "ranking"]}),
        ("User Information", {"fields": ["user"]}),
    ]
    list_display = ["user", "artist_name", "song_name", "ranking"]


admin.site.register(Record, RecordAdmin)
