from django.contrib import auth, messages
from django.contrib.auth import get_user_model
from rest_framework import status
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import UserLoginSerializer, UserSignupSerailizer, MyInfoSerializer, UserDetailSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token


from rest_framework.views import APIView
from django.utils import timezone

class UserLoginView(generics.GenericAPIView): # 로그인
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return get_user_model().objects.none()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(): # 유효성 검사
            return Response(serializer.errors)
        user = serializer.validated_data

        token, created = Token.objects.get_or_create(user=user)
        
        response_data = {
            "message": "Login successful.",
            "user": {
                "id": user.id,
                "username": user.username,
                "token": token.key,
                "is_staff" : user.is_staff
            }
        }
        return Response(response_data, status=HTTP_200_OK)

class UserLogoutView(APIView): # 로그아웃
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            # 로그인된 사용자에 대해서만 로그아웃 처리
            request.user.is_active = False
            request.user.last_logout = timezone.now()
            request.user.save()
            response_data = {
                "message": "Logout successful."
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # 익명 사용자에 대한 처리
            response_data = {
                "message": "You are not logged in."
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

class UserSignupView(generics.GenericAPIView): # 회원가입
    serializer_class = UserSignupSerailizer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return get_user_model().objects.none()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = {
            "message": "Signup successful."
        }
        return Response(response_data, status=HTTP_200_OK)


class MyInfoView(APIView):
    def get(self, request, username, format=None):
        user = get_user_model().objects.filter(username=username).first()
        if user:
            serializer = MyInfoSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class UserListView(APIView):
    def get(self, request, format=None):
        if request.user.is_staff:
            users = get_user_model().objects.all()
            serializer = UserDetailSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

class UserUpdateView(APIView):
    def patch(self, request, pk, format=None):
        if request.user.is_staff:
            try:
                user = get_user_model().objects.get(pk=pk)
            except get_user_model().DoesNotExist:
                return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = UserDetailSerializer(user, data=request.data, partial=True)  # partial=True로 설정하여 부분 업데이트를 가능하게 함
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

def logout(request):
    auth.logout(request)
    messages.info(request, '로그아웃 되었습니다.')
    return redirect('/main/')

