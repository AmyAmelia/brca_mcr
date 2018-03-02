from django.shortcuts import render
from db.models import *
import pandas as pd
# from bokeh.io import show, output_file
# from bokeh.models import ColumnDataSource
# from bokeh.palettes import Spectral6
# from bokeh.plotting import figure
# from bokeh.transform import factor_cmap
# from bokeh.resources import CDN
# from bokeh.embed import components


def home(request):
    ''' sets direct to home page '''
    return render(request, 'db/home.html')


def variant(request):
    '''renders contents if database into table'''
    # collect all data
    patient = Patient.objects.all()

    # collect unique cancer types as a list and get counts for each
    types = [x.description for x in Description.objects.all()]
    type_counts = [len(patient.filter(id_description__description=t)) for t in types]
    # collect unique cancer stages as a list and get counts for each
    stages = [x.stage_str for x in Stage.objects.all()]
    stage_counts = [len(patient.filter(id_stage__stage_str=s)) for s in stages]

    stages = [stages[2], stages[0], stages[1]]
    stage_counts = [stage_counts[2], stage_counts[0], stage_counts[1]]
    stage_d = {'one':'1', 'two':'2', 'three':'3'}
    stages_num = [stage_d[x] for x in stages]

    # plots - type
    type_source = ColumnDataSource(data=dict(types=types, counts=type_counts))
    type_p = figure(x_range=types, plot_height=300, plot_width=500, toolbar_location=None, title="Number of cases")
    type_p.vbar(x='types', top='counts', width=0.9, source=type_source,
           line_color='white', fill_color=factor_cmap('types', palette=['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#deebf7', '#f7fbff'], factors=types))
    type_p.xgrid.grid_line_color = None
    type_p.y_range.start = 0
    type_p.y_range.end = 15
    type_p.legend.orientation = "horizontal"
    type_p.legend.location = "top_center"
    type_script, type_div = components(type_p, CDN)

    # plots - stage
    stage_source = ColumnDataSource(data=dict(types=stages, counts=stage_counts))
    stage_p = figure(x_range=stages, plot_height=300, plot_width=500, toolbar_location=None, title="Number of cases")
    stage_p.vbar(x='types', top='counts', width=0.9, source=stage_source,
           line_color='white', fill_color=factor_cmap('types', palette=['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#deebf7', '#f7fbff'], factors=types))
    stage_p.xgrid.grid_line_color = None
    stage_p.y_range.start = 0
    stage_p.y_range.end = 40
    stage_p.legend.orientation = "horizontal"
    stage_p.legend.location = "top_center"
    stage_script, stage_div = components(stage_p, CDN)

    return render(request, 'db/variant.html', {'patient': patient, 'type_counts': type_counts, 'stage_counts': stage_counts, 'type_script':type_script, 'type_div':type_div, 'stage_script':stage_script, 'stage_div':stage_div})
    #return render(request, 'db/variant.html', {'patient': patient, 'type_counts': type_counts, 'stage_counts': stage_counts})
