from django.contrib.auth import get_user_model

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializer import UserSerializer

User = get_user_model()

# Register Account
class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data
            name = data['name']
            email = data['email'].lower()
            password = data['password']

            # If user exists
            if not User.objects.filter(email=email).exists():
                # Create user
                User.objects.create_user(
                    name=name, email=email, password=password
                )
                return Response(
                    {'success': 'ユーザーの作成に成功しました'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'error': 'すでに登録されているメールアドレスです'},
                    status=status.HTTP_400_BAD_REQUEST
                )


        except:
            return Response(
                {'error': 'アカウント登録時に問題が発生しました'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Get user info
