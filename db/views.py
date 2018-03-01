from django.shortcuts import render
from db.models import *
from django.db import connection


def home(request):
    ''' sets direct to home page '''
    return render(request, 'db/home.html')

def sql_query(q):
    cursor = connection.cursor()
    cursor.execute(q)
    row = cursor.fetchall()
    return row

def variant(request):
    '''renders contents if database into table'''
    patient = Patient.objects.all()
    return render(request, 'db/variant.html', {'patient':patient})
