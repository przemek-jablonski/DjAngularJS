from rest_framework import serializers

from authentication.serializers import UserAccountSerializer
from entries.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    author = UserAccountSerializer(read_only=True, required=False)

    class Meta:
        model = Entry
        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        # possible null pointer here ( .get_validation...() )
        exclusions = super(EntrySerializer, self).get_validation_exclusions()
        return exclusions + ['author']