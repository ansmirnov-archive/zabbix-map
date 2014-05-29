from django.shortcuts import render_to_response
from main import models
import widgets as widgets_


def home(request):
    return render_to_response('home.html')


def items(request):
    return render_to_response('items.json', {
        'items': models.Switch.objects.all()
    })

def widgets(request, point_id):
    point_id = int(point_id)
    try:
        switches = models.Point.objects.get(id=point_id).switch_set.all()
    except:
        switches = []
    res = []
    for sw in switches:
        res.append(widgets_.switch(sw))
    return render_to_response('widgets.json', {
        'widgets': res
    })