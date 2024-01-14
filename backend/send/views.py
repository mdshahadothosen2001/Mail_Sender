from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from send.send_mail import sendMail


class SendMailView(APIView):
    """This class used for sending mail content to any mail address"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        sendMail(request)

        return Response(
            {"message": "Successfully send your message to this mail address!"}
        )
