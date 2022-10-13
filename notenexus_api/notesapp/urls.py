from django.contrib import admin
from django.urls import path

from notesapp.views import CreateNodeView, NodeView, NoteView

urlpatterns = [
    path('nodeCreate', CreateNodeView.as_view(), name='createNode'),
    path('nodes', NodeView.as_view(), name='nodes'),
    path('nodes/<str:pk>', NodeView.as_view(), name='nodes'),
    path('notes', NoteView.as_view(), name='notes'),
    path('notes/<str:pk>', NoteView.as_view(), name='notes')
]