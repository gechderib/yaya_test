from django.urls import path
from .views import WebhookEndpoint

urlpatterns = [
    path('webhook/', WebhookEndpoint.as_view(), name='webhook-endpoint'),
]
