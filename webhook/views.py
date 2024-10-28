import os
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WebhookPayloadSerializer
from .utils import verify_signature
from .models import WebhookPayload

class WebhookEndpoint(APIView):
    def post(self, request, *args, **kwargs):
        # Get the signature from the headers
        received_signature = request.headers.get("YAYA-SIGNATURE")
        secret_key = os.getenv("YAYA_WEBHOOK_SECRET", "")
        print("received_signature: v " + received_signature)
        print("secret_key: v" + secret_key)
        # Verify signature
        if not verify_signature(request.data, received_signature, secret_key):
            return Response({"detail": "Invalid signature"}, status=status.HTTP_403_FORBIDDEN)

        # Serialize and save payload
        serializer = WebhookPayloadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Webhook received and processed"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
