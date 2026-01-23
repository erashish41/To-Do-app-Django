from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(email, username):
    subject = "Welcome back "
    message = f"Hi {username},\n\nWelcome back to your To-Do App!"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
