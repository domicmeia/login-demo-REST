from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from login.apps.accounts.api.permissions import IsNotAuthenticated
from login.apps.accounts.api.v1.serializers.login import LoginSerializer
from login.apps.accounts.services.login import LoginService


class LoginView(GenericAPIView):
    permission_classes = [IsNotAuthenticated]
    serializer_class = LoginSerializer

    @extend_schema(summary="Login", tags=["Accounts"], responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()})
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        response = LoginService.login(request, user)
        return response


class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(summary="Log out", tags=["Accounts"], responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()})
    def post(self, request):
        response = LoginService.logout(request)
        return response
