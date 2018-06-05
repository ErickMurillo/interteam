from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def editar_contraparte(request, slug, template='admin/editar_contraparte.html'):
	contra = get_object_or_404(Contraparte, slug=slug)

	if request.method == 'POST':
		form = ContraparteForms(data=request.POST, 
								instance=contra, 
								files=request.FILES)
		if form.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.user = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/accounts/profile/')
	else:
		form = ContraparteForms(instance=contra)

	return render(request, template, locals())


