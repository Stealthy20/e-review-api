from rest_framework import generics, permissions
from review_api.permissions import IsOwnerOrReadOnly
from keep.models import Keep
from keep.serializers import KeepSerializer


class KeepList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = KeepSerializer
    queryset = Keep.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KeepDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = KeepSerializer
    queryset = Keep.objects.all()
