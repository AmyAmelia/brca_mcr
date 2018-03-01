from django.shortcuts import render
from db.models import *


def home(request):
    ''' sets direct to home page '''
    return render(request, 'db/home.html')


def variant(request):
    '''renders contents if database into table'''
    patient = Patient.objects.all()
