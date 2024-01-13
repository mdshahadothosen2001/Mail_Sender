from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from django.core.mail import send_mail

from config.EMAIL_HOST import EMAIL_HOST_USER


def sendMail(request):

    email = request.data.get("email")
    subject = request.data.get("subject", ' ')
    body = request.data.get("body", ' ')

    if not email:
        raise ValidationError("Can't send without mail address")
    
    try:
        send_mail(subject, body, EMAIL_HOST_USER, [email])
    except:
        return Response("Email Address not found! Please double check.")
    
    