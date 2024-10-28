from rest_framework import serializers
from .models import WebhookPayload

class WebhookPayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookPayload
        fields = '__all__'
