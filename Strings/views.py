from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from Strings.models import Example
# Create your views here.

modules=['list','string','tuple','set','dictionary']
def index(request):
    return render(request,"Strings/base_layout.html",{'modules':modules})

def Methods(request,obj):
    colors = ['primary','secondary','success','danger','warning','info','dark']
    objs = {
        'list':list,
        'dictionary':dict,
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
            'magic':magic_methods,
            'modules':modules
        }
    return render(request,"Strings/methods.html",params)

def Details(request,btn_id):
    obj_type = {
        'list':'list','dict':'dict','tuple':'tuple','set':'set','string':'str'
    }
    classes,method=btn_id.split("-")
    types = obj_type[classes]
    exam=Example.objects.get(ex_id=2)
    

    document = eval(f'{types}.{method}.__doc__')
    data = {

        
        'Defination':document,
        'Syntax':exam.syntax,
        'Example':exam.example,
        'Output':exam.output
    }
    params={
        'type':types,
        'names':btn_id.split("-"),
        'modules':modules,
        'data':data
    }
    return render(request,'Strings/details.html',params)