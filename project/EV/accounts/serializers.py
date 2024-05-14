from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model, logout
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'phone']


from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("no data")

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            if user.is_active == 0:
                if user.is_approved:
                    user.is_active = 1
                    user.login() #로그인 메소드 시작
                    user.save()
                    return user
                else:
                    print("pending approval")
                    raise serializers.ValidationError({"auth_error":"pending approval"}) 
            else:
                print("using")
                raise serializers.ValidationError({"auth_error":"using"}) # 
        else:
            print("id pw error")
            raise serializers.ValidationError({"auth_error":"id pw error"})


class UserSignupSerailizer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'name', 'phone']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    phone = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        name = data.get('name')
        phone = data.get('phone')

        if not username or not password or not name or not phone:
            raise serializers.ValidationError("모든 값을 입력하세요.")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("이미 존재하는 아이디입니다.")

        return data


class UserLogoutSerializer(serializers.Serializer):
    def logout(self, request):
        logout(request)
        return request.user