from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from agendas.models import *

# Create your views here.
@login_required
def perfil(request,template='perfil.html'):
    foros = Foros.objects.filter(contraparte_id=request.user.id)
    agendas = Agendas.objects.filter(user_id=request.user.id)

    return render(request, template, locals())
