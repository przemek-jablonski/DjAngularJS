from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from entries.models import Entry
from entries.permissions import IsAuthorOfPost
from entries.serializers import EntrySerializer

# CRUD
class EntryViewSet(viewsets.ModelViewSet):
    # todo: make custom ordering
    queryset = Entry.objects.order_by('-created_at')

    serializer_class = EntrySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
           return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAuthorOfPost())

    def perform_create(self, serializer):
        instance = serializer.save(author = self.request.user)
        # instance2 = serializer.save(title = self.request.title)
        return super(EntryViewSet, self).perform_create(serializer)


class UserAccountEntriesViewSet(viewsets.ViewSet):
    queryset = Entry.objects.select_related('author').all()
    serializer_class = EntrySerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)
        if serializer.data.__len__() == 0:
            return Response({
                'status': 'no content',
                'message': 'no content.'
            }, status=status.HTTP_204_NO_CONTENT);
        return Response(serializer.data)