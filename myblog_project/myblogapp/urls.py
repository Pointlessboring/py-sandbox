"""Define URL patterns for myblogapp."""

from django.urls import path
from . import views

app_name = 'myblogapp'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('titles/', views.titles, name='titles'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('entry/<int:entry_id>/', views.entry, name='entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]