from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer
# Create your views here.

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    # Set permission to allow only authenticated users to view notifications
    permission_classes = [permissions.IsAuthenticated]
    
    # Define the serializer class for the Notification model
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # Return all notifications for the authenticated user, ordered by timestamp
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')