from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic
from PIL import Image

from scales1 import scales
from .models import Fretboard

#scale = 'F'
#tunings = ['E', 'A', 'D', 'G', 'B', 'E']


def SelectBoard(request):
    #model = Fretboard
    return render(request, 'scales_app/select_board.html')

def GenBoard(request):
    fretboard = request.POST

    img_scale = 1

    size = (int(1080*img_scale),int(200*img_scale))

    #print(fretboard)

    tunings = []

    scale = fretboard['scale']

    tunings.append(fretboard['string1'])
    tunings.append(fretboard['string2'])
    tunings.append(fretboard['string3'])
    tunings.append(fretboard['string4'])
    tunings.append(fretboard['string5'])
    tunings.append(fretboard['string6'])

    img = scales.gen_board(scale, tunings)
    img = img.resize(size)

    response = HttpResponse(content_type = "image/bmp")
    img.save(response, "BMP")
    return response

    #return HttpResponseRedirect(reverse('scales_app:SelectBoard'))
