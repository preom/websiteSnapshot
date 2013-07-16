# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from screenshot import Screenshot
from PIL import Image
from pyvirtualdisplay import Display
from ghost import Ghost
import os


def index(request):
    dir_name = os.path.dirname(__file__)
    img_name = os.path.join(dir_name, 'pic.jpg')

    if request.method == 'POST':
        url = request.POST.get('url', '')
    else:
        url = request.GET.get('url', '')
    
    if not url:
        url = 'http://www.bbc.uk.com'

    

    display = Display()
    display.start()

    ghost = Ghost()
    ghost.open(url)
    width = int(ghost.evaluate('document.body.clientWidth')[0])
    height = int(ghost.evaluate('document.body.clientHeight')[0])

    ghost = Ghost(viewport_size=(width, height))
    ghost.open(url)
    ghost.capture_to(img_name, selector='body')

    image =  Image.open(img_name) 
    image.thumbnail((128, 128), Image.ANTIALIAS)

    response = HttpResponse(mimetype='image/jpeg')
    image.save(response, 'jpeg')

    display.stop()

    return response
