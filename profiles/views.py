from rest_framework.views import APIView
from django.db.models import Count
from rest_framework import generics, filters
from django.http import Http404
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from review_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        reviews_count=Count('owner__review', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = ['reviews_count']


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        reviews_count=Count('owner__review', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
