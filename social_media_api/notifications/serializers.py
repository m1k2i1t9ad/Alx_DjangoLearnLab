# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'timestamp', 'target_ct', 'target_id']  # Adjust fields as necessary