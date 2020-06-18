from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from myapp.serializers import LoginSerializer, RegisterSerializer


class UserViewSet(viewsets.ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response({
            'message': f'Hello {request.user.username}!'
        })

    def create(self, request):
        raise PermissionDenied('This method no support for this case.')

    def retrieve(self, request, pk=None):
        raise PermissionDenied('This method no support for this case.')

    def update(self, request, pk=None):
        raise PermissionDenied('This method no support for this case.')

    def partial_update(self, request, pk=None):
        raise PermissionDenied('This method no support for this case.')

    def destroy(self, request, pk=None):
        raise PermissionDenied('This method no support for this case.')

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.get_dict(), status=200)

        return Response(serializer.errors, status=401)

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Register success'}, status=200)

        return Response(serializer.errors, status=400)


