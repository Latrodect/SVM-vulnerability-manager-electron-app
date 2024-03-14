from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


from ..request_serializers.auth_serializer import UserLoginSerializer
from ..request_serializers.register_serializer import UserRegistrationSerializer

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        User = get_user_model()
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if not user:
               User.objects.create_user(
                username=username,
                email=email,
                password=password
                )
               return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message':'User already exist'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=201)
    return Response(serializer.errors, status=400)