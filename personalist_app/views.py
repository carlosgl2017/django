from django.shortcuts import render
from personalist_app.models import Persona
from django.http import JsonResponse
# Create your views here.
def persona_list(request):
    personas = Persona.objects.all()
    data={
        'personas':list(personas.values())
    }
    
    return JsonResponse(data)