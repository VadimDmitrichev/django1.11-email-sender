# coding=utf-8
from celery import shared_task
from time import sleep

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template


@shared_task
def sleepy(duration):
	sleep(duration)
	return None


@shared_task
def send_email_task(first_name, last_name, email):
	sleep(10)
	subject = 'Подписка на email рассылку'
	from_email = settings.EMAIL_HOST_USER
	to_email = (email, email)
	context = {
		'first_name': first_name,
		'last_name': last_name
	}
	message = get_template('send_email/mail.html').render(context)
	msg = EmailMessage(subject, message, to=to_email, from_email=from_email)
	msg.content_subtype = 'html'
	msg.send()
	return None
