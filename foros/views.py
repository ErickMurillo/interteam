from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from agendas.models import *
from django.shortcuts import get_object_or_404
from contrapartes.models import *

# Create your views here.
@login_required
def perfil(request,template='admin/perfil.html'):
	user = request.user.id
	user_profile = get_object_or_404(UserProfile, user = user)
	contraparte = get_object_or_404(Contraparte, id = user_profile.contraparte.id)
	
	foros = Foros.objects.filter(contraparte_id=request.user.id)
	agendas = Agendas.objects.filter(user_id=request.user.id)

	return render(request, template, locals())
