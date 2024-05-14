from django.contrib import auth, messages
from django.contrib.auth import get_user_model
from rest_framework import status
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import UserLoginSerializer, UserSignupSerailizer
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
                "token": token.key
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



#def signup(request):
#    if request.method == 'POST':
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('/main/')
#        else:
#            print(form.errors)
#    else:
#        form = SignUpForm()
#    return render(request, 'signup.html')

#@csrf_exempt
#def login(request):
#    if request.method == 'POST':
#        form = loginForm(request.POST)
#        if form.is_valid():
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password']
#            user = authenticate(username=username, password=password)
#            if user is not None:
#                if user.is_approved:
#                    auth.login(request, user)
#                    print('로그인 성공')
#                    return JsonResponse({'status': 'success'})
#                else:
#                    print('승인 대기 중')
#                    return JsonResponse({'status': 'error', 'message': '승인 대기 중입니다.'})
#            else:
#                print('로그인 실패')
#                return JsonResponse({'status': 'error', 'message': '잘못된 아이디, 비밀번호 입니다.'})
#    return JsonResponse({'status': 'error', 'message': 'Invalid method'})

def logout(request):
    auth.logout(request)
    messages.info(request, '로그아웃 되었습니다.')
    return redirect('/main/')

