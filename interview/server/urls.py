from . import views
from django.urls import include, path


urlpatterns = [
    path('messages/', views.insert_messages, name='insert_messages'),
    path('conversations/<int:id>', views.get_message, name='get_message'),
]
