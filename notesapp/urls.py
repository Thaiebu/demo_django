from django.urls import path
from .views import home, notesapp, create_notes

urlpatterns = [
    path('', home),
    path('notes/', notesapp),
    path('sites/', create_notes)
]
