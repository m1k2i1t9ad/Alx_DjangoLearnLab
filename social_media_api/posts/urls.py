from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,FeedViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
# router.register(r'feed', FeedViewSet,basename='feed')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedViewSet.as_view({'get': 'list'}), name='feed'),  # Explicitly add the feed endpoint
]