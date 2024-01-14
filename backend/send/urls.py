from django.urls import path

from .views import SendMailView


urlpatterns = [
    # localhost/send/mail/
    path(route="mail/", view=SendMailView.as_view(), name="send-mail")
]
