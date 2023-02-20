from django.db import IntegrityError
from rest_framework import serializers
from keep.models import Keep


class KeepSerializer(serializers.ModelSerializer):
    """
    Serializer for the Save model
    The create method handles the unique constraint on 'owner' and 'review'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Keep
        fields = ['id', 'created_at', 'owner', 'review']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })