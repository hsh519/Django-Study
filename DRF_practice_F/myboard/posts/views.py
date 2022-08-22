from rest_framework import viewsets

from .serializers import CreatePostSerializer
from .serializers import PostSerializer
from .permissions import CustomReadOnly
from .models import Post
from users.models import Profile

# Create your views here.

class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()
    permission_class = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return PostSerializer
        return CreatePostSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)