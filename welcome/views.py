import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from . import main

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())


def searchflight(request):
    response = "{  "botkitVersion": "0.4.0",  "messages": [ { "_type": "TextMessage", "text": "Hello" } ] }"
    return HttpResponse(response)
    #return HttpResponse(main.amadeus_flight_search_webhook(request.body))
