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
    q = 'select patient.name, patient.age, description.description, stage.stage, platform.platform, variant.cdna, variant.protein, variant.genomic from patient inner join description on patient.id_description = description.id_description inner join stage on patient.id_stage = stage.id_stage inner join platform on patient.id_platform = platform.id_platform inner join variant on patient.id_variant = variant.id_variant;'
    data = sql_query(q)
    patient = Patient.objects.all()
    dlist = []
    for d in data:
        dic = {}
        dic['name'] = d[0]
        dic['age'] = d[1]
        dic['description'] = d[2]
        dic['stage'] = d[3]
        dic['platform'] = d[4]
        dic['cdna'] = d[5]
        dic['protein'] = d[6]
        dic['genomic'] = d[7]
        dlist.append(dic)

    return render(request, 'db/variant.html', {'vdata':dlist})
