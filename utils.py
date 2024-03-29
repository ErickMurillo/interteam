# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse 
import json as simplejson
import os
import re

# ugly code but usefull
to_choices = lambda x: [(y,unslugify(y)) for y in x]

def unslugify(value):
    return ' '.join([s.capitalize() \
                     if i == 0 else s \
                     for i, s in enumerate(value.split('_'))])
    
def save_as_xls(request):
    tabla = request.POST['tabla']    
    response = render('xls.html', {'tabla': tabla, })
    response['Content-Disposition'] = 'attachment; filename=tabla.xls'
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Charset'] ='UTF-8'
    return response

p = re.compile(r'[^0-9a-zA-Z\._]+')

# metodo para reemplazar los caracteres especiales en una cadena
def repl(match):
    chars = {u'á': u'a', u'Á':u'A', u'é':u'e', u'É':u'E', u'í': u'i', u'Í':u'I', u'ó':u'o', u'Ó':'O', u'ú':u'u', u'Ú':'U', u'ñ':u'n', u'ü':u'u'}
    a = ''
    for i in match.group():
        if i in chars:
            a = a + chars[i]
        else:
            a = a + '_'
    return a

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    nombre = p.sub(repl, filename.split('.')[-2])
    filename = "%s.%s" % (nombre, ext)
    return os.path.join(instance.fileDir, filename)

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    nombre = p.sub(repl, filename.split('.')[-2])
    filename = "%s.%s" % (nombre, ext)
    return os.path.join(instance.imgDir, filename)