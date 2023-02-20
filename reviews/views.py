from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from review_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    """
    List Reviews or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        'keep__owner__profile',
        'owner__profile',
        'category'
    ]

    search_fields = [
        'owner__username',
        'title',
        'category',
        'rating',
    ]

    ordering_fields = [
        'keep__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a review and edit or delete it if you own it.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()

    