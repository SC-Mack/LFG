from rest_framework import viewsets

from main.api.permissions import IsAuthorOrReadOnly
from main.models import Review
from main.api.serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-date_created')
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = ReviewSerializer
    lookup_field = 'slug'
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)