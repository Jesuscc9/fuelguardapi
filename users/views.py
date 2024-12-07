from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from knox.views import LogoutAllView
from drf_yasg import openapi
from knox.models import AuthToken


from . import serializers
from .models import Profile

User = get_user_model()


class UserRegisterationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new User.
    """

    permission_classes = (AllowAny,)
    serializer_class = serializers.UserRegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """

    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer

    @swagger_auto_schema(
        operation_description="Authenticate a user using email and password.",
        request_body=serializers.UserLoginSerializer,
        responses={
            200: openapi.Response(
                description="Authentication successful",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "user": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, description="User ID"
                                ),
                                "email": openapi.Schema(
                                    type=openapi.TYPE_STRING, description="User email"
                                ),
                            },
                        ),
                        "token": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Knox authentication token",
                        ),
                    },
                ),
            ),
            400: "Invalid credentials",
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data  # Autenticación exitosa

        # Generar token con Knox
        token = AuthToken.objects.create(user)[1]

        return Response(
            {
                "user": {
                    "id": user.id,
                    "email": user.email,
                },
                "token": token,
            },
            status=200,
        )


class UserLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout users by invalidating their refresh token.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LogoutSerializer

    @swagger_auto_schema(
        operation_description="Logout the user by blacklisting their refresh token.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "refresh": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Refresh token to be blacklisted",
                ),
            },
            required=["refresh"],
        ),
        responses={
            205: "Logout successful",
            400: "Invalid token or request",
        },
    )
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAllAPIView(LogoutAllView):
    """
    An endpoint to logout the user from all sessions.
    """

    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="Logout the user from all active sessions.",
        responses={
            205: "Logout from all sessions successful",
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user information
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CustomUserSerializer

    def get_object(self):
        return self.request.user


class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user profile
    """

    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile


class UserAvatarAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user avatar
    """

    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileAvatarSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile
