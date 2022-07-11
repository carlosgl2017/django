from django.urls import path
from personalist_app.views import persona_list
urlpatterns = [
     path('list/',persona_list, name='persona-list'),
]
 