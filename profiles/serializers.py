from rest_framework import serializers
from .models import Profile
from keep.models import Keep


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    The create method handles the reviews count.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    reviews_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'image',
            'is_owner', 'reviews_count',
        ]
