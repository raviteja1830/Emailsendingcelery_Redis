from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .task import *
from .email import *




def index(request):
    send_mail_task.delay()
    return HttpResponse('<h1>Mail has been sent</h1>')



