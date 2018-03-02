from django.shortcuts import render
from db.models import *
from django.db import connection
import myvariant

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
    patient = Patient.objects.all
    return render(request, 'db/variant.html', {'patient':patient})

# def variant_ann (request):
# 	''' Pulls variant annotation for variant.info and passes variables to html'''
# 	mv = myvariant.MyVariantInfo()
# 	var_out = mv.getvariant('chr17:' + genome, ['dbsnp.rsid', 'cadd.polyphen.cat', 'cadd.sift.cat', 'gnomad_exome.af.af'])

# print (var_out)
# for lv_one in var_out:
#     print("lv_one", lv_one)
#     if 'version' in lv_one:
#         pass
#     else:
#         print (var_out['gnomad_exome']['af']['af'])