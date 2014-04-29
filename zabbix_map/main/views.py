from django.shortcuts import render_to_response
from main import models


def home(request):
    return render_to_response('home.html')


def items(request):
    return render_to_response('items.json', {
        'items': models.Switch.objects.all()
    })