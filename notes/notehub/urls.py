from django.urls import path
from . import views

app_name = 'notehub'


urlpatterns = [
    path('',views.index,name="index"),
    path('my-notes/',views.my_notes,name='my-notes'),
    path('create-notes/',views.create_note_view,name="create-notes"),
    path('edit-note/<slug:slug>/',views.edit_note_view,name='edit-note'),
    path('delete-note/<slug:slug>/',views.delete_note_view,name='delete-note'),
    path('category/<slug:slug>/',views.category_note_view,name="category"),
]

