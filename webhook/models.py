from django.db import models
import uuid 

class WebhookPayload(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_at_time = models.BigIntegerField()
    timestamp = models.BigIntegerField()
    cause = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    invoice_url = models.URLField()

    def __str__(self):
        return f"WebhookPayload {self.id} - {self.amount} {self.currency}"
