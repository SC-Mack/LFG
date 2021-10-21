from rest_framework import viewsets

from main.api.permissions import IsAuthorOrReadOnly
from main.models import Review
from users.models import CustomUser
from main.api.serializers import ReviewSerializer
from main.api.serializers import CustomUserSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-date_created')
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = ReviewSerializer
    lookup_field = 'slug'
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = CustomUserSerializer
    lookup_field = 'slug'
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)