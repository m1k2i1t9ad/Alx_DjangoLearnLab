# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, CustomAuthToken

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('login/', CustomAuthToken.as_view(), name='login'),
# ]

from django.urls import path
from .views import UserRegisterView, UserLoginView
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]