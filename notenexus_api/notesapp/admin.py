from django.contrib import admin

from notesapp.models import Note, Node

# Register your models here.
admin.site.register(Node)
admin.site.register(Note)