from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from agendas.models import *
from django.shortcuts import get_object_or_404
from contrapartes.models import *
from notas.models import *
from agendas.models import *
from galerias.models import *

# Create your views here.
@login_required
def perfil(request,template='admin/perfil.html'):
	user = request.user.id
	user_profile = get_object_or_404(UserProfile, user = user)
	contraparte = get_object_or_404(Contraparte, id = user_profile.contraparte.id)
	
	foros = Foros.objects.filter(contraparte_id=request.user.id)
	agendas = Agendas.objects.filter(user_id=request.user.id)

	#estadisticas
	notas_count = Notas.objects.filter(user = request.user).count()
	eventos_count = Agendas.objects.filter(user = request.user).count()
	galerias_img = GaleriaImagenes.objects.filter(user = request.user).count()
	galerias_vid = GaleriaVideos.objects.filter(user = request.user).count()
	galerias_count = galerias_img + galerias_vid
	participacion_foros = Aportes.objects.filter(user = request.user).count()

	return render(request, template, locals())
