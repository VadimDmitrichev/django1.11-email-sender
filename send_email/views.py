# coding=utf-8
from django.shortcuts import render
from .forms import SubscriberForm
from .models import Subscriber
from .tasks import sleepy, send_email_task


def home(request):
	if request.method == 'GET':
		return render(request, 'send_email/home.html', {'form': SubscriberForm()})
	else:
		try:
			form = SubscriberForm(request.POST)
			if form.is_valid():
				new_subscriber = form.save(commit=False)
				new_subscriber.save()
				send_email_task.delay(request.POST['first_name'], request.POST['last_name'], request.POST['email'])
			return render(request, 'send_email/success.html')
		except ValueError:
			return render(request, 'send_email/home.html', {'form': SubscriberForm, 'error': 'Скорее всего вы ввели '
																							 'email который уже '
																							 'используется'})

