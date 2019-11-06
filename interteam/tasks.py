# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task,Task
import os, fnmatch
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from foros.models import *
from contrapartes.models import *

class CallbackTask(Task):
	def on_success(self, retval, task_id, args, kwargs):
		foro = get_object_or_404(Foros, id=retval)
		foro.correo_enviado = True
		foro.save()

@shared_task(default_retry_delay=10, max_retries=3, base=CallbackTask)
def send_mail_foro(id,user):
	foro = get_object_or_404(Foros, id=id)
	subject, from_email = 'Nuevo foro', 'cluster.nicaragua@gmail.com'
	text_content = render_to_string('email/foro.txt', {'foro': foro,})

	html_content = render_to_string('email/foro.txt', {'foro': foro,})

	list_mail = UserProfile.objects.exclude(user__id = user).values_list('user__email',flat=True)

	msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
	msg.attach_alternative(html_content, "text/html")
	msg.send()

	print(foro.id)
	return foro.id
