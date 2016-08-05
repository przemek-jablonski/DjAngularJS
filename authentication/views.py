from django.contrib.auth import authenticate, login
import json
from django.shortcuts import render

from authentication.permissions import IsAccountOwner
from authentication.serializers import UserAccountSerializer
from authentication.models import UserAccount

from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework import status, views

# from django.http import HttpResponse
# import datetime


# views in django:
#   Python function that TAKES a web request and RETURNS web response
#   request: like an API endpoint
#   response: HTML contents, redirect, 404, JSON/XML file etc.
#   view funcions include any additional logic needed to return a response
# example:
# def current_datetime(request):
#     now = datetime.datetime.now()
#     html_body = "<html><body>Current time: %s.</body></html>" % now
#     return HttpResponse(html_body)


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
            return Response(serializer.validated_data, status = status.HTTP_201_CREATED)

        return Response({
            'status': '400 Bad API Request',
            'message': 'User data not completed or already exist in database.'},
            status=status.HTTP_400_BAD_REQUEST)


# extending views.APIView (more generic class than ModelViewSet)
# class will be more low-level, since 'logging in' is an operation which is
# not very similar to creating()-updating() objects.
class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = UserAccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)




