from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Registration
from django.core.signing import TimestampSigner

@shared_task
def verify_email(email,registration_id):
    regist = Registration.objects.get(id = registration_id)    
    
    signer = TimestampSigner()
    token = signer.sign(regist.id)
    link = f"http://127.0.0.1:8000/verify/{token}/" 

    subject = "Verificación de correo - Sorteo de San Valentín "
    message = f"Hola {regist.name},\n haz clic en el enlace para confirmar tu correo: {link}"

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, email)
    return f"Correo de verificación enviado a {email}"


@shared_task
def send_winner_email(email, full_name):
    subject = "¡Felicidades! Has ganado el sorteo de San Valentín"
    message = f"Hola {full_name},\n ¡Felicidades! Has sido seleccionado como el ganador del sorteo de San Valentín. Nos pondremos en contacto contigo pronto con más detalles."
    
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
    return f"Correo de ganador enviado a {email}"

