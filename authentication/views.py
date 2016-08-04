from django.shortcuts import render

from authentication.permissions import IsAccountOwner
from authentication.serializers import UserAccountSerializer
from authentication.models import UserAccount

from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework import status

from django.http import HttpResponse
import datetime


# views in django:
#   Python function that TAKES a web request and RETURNS web response
#   request: like an API endpoint
#   response: HTML contents, redirect, 404, JSON/XML file etc.
#   view funcions include any additional logic needed to return a response
# example:
def current_datetime(request):
    now = datetime.datetime.now()
    html_body = "<html><body>Current time: %s.</body></html>" % now
    return HttpResponse(html_body)


# creating viewset (set of views)
# ModelViewSet gives us interface for CRUD operations on a given model
class AccountViewSet(viewsets.ModelViewSet):

    # 'username' (not ID) to be able to identify accounts by username instead
    lookup_field = 'username'
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()

    def get_permissions(self):
        # allow any user access to safe methods in API endpoints
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        # allow any user to POST (ie. create an account)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            UserAccount.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data,status = status.HTTP_201_CREATED)

        return Response(
            {'status': '400 Bad API Request',
            'message': 'Invalid data for account creation'},
            status = status.HTTP_400_BAD_REQUEST)
