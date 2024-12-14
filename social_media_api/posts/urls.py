from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,FeedViewSet,LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
# router.register(r'feed', FeedViewSet,basename='feed')


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedViewSet.as_view({'get': 'list'}), name='feed'),  # Explicitly add the feed endpoint
    path('<int:pk>/like/', LikeViewSet.as_view({'post': 'create'}), name='like_post'),   # URL for liking a post
    path('<int:pk>/unlike/', LikeViewSet.as_view({'delete': 'destroy'}), name='unlike_post'),  # URL for unliking a post
]