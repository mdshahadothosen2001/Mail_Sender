from django.urls import path

from .views import SendMailView


urlpatterns = [
    # localhost:8093/send/mail/
    path(route="mail/", view=SendMailView.as_view(), name="send_mail")
]
