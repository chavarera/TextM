from django.shortcuts import render
from django.http import HttpResponse
from random import randint
# Create your views here.

def index(request):
    return render(request,"Strings/base_layout.html")

def Methods(request,obj):
    colors = ['primary','secondary','success','danger','warning','info','dark']
    objs = {
        'list':list,
        'dict':dict,
        'tuple':tuple,
        'set':set,
        'string':str
    }
    params = {}
    if obj in objs.keys():
        data = {method:"btn btn-"+colors[randint(0,len(colors)-1)] for method in dir(objs[obj]) if method[0]!='_'}
        magic_methods = {method:"btn btn-"+colors[randint(0,len(colors)-1)] for method in dir(objs[obj]) if method.startswith('__')}
        params = {
            'names':obj,
            'data':data,
            'magic':magic_methods
        }
    return render(request,"Strings/methods.html",params)

def Details(request,btn_id):
    obj_type = {
        'list':'list','dict':'dict','tuple':'tuple','set':'set','string':'str'
    }
    classes,method=btn_id.split("-")
    types = obj_type[classes]
    
    document = eval(f'{types}.{method}.__doc__')
    params={
        'names':btn_id.split("-"),
        'docs':document,
        'type':types
    }
    return render(request,'Strings/details.html',params)