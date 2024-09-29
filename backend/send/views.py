from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from send.send_mail import SendMail


class SendMailView(APIView):
    """This class used for sending email content to any email address"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        SendMail(request)

        return Response(
            {"message": "Successfully send your message to this email address!"}
        )
