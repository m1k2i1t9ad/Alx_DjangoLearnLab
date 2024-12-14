from django.shortcuts import render
from rest_framework import viewsets, permissions,generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404
class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = PostFilter
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
    

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get posts from users that the current user follows
        followed_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    

class LikeViewSet(viewsets.ModelViewSet):
    # Set permission to allow only authenticated users
    permission_classes = [permissions.IsAuthenticated]

    # Define the serializer class for the Like model
    serializer_class = LikeSerializer  # Create a serializer for the Like model

    def get_queryset(self):
        # Return all likes made by the authenticated user
        return Like.objects.filter(user=self.request.user)

    def create(self, request, post_id=None):
        # Retrieve the post being liked by its ID
        post =get_object_or_404(Post,id=post_id)
        
        # Try to create a Like object; if it exists, retrieve it
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification if the like was newly created
            Notification.objects.create(
                recipient=post.author,  # The post's author receives the notification
                actor=request.user,     # The user who liked the post
                verb='liked your post', # Description of the action
                target_ct=ContentType.objects.get_for_model(Post),  # Content type for the target (Post)
                target_id=post.id       # ID of the target post
            )
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        
        # If the like already exists, return a message indicating so
        return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, post_id=None):
        # Retrieve the post being unliked by its ID
        post = get_object_or_404(Post,id=post_id)
        
        # Attempt to find the Like object for the authenticated user and post
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            # If a like exists, delete it
            like.delete()
            return Response({"message": "Post unliked."}, status=status.HTTP_204_NO_CONTENT)
        
        # If no like was found, return a message indicating so
        return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)