from django.contrib.auth.models import User # 기본 유저 모델
from django.contrib.auth.password_validation import validate_password # 장고의 기본 패스워드 검증 도구

from rest_framework import serializers # 시리얼라이저
from rest_framework.authtoken.models import Token # 토큰 모델
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True, # 무조건 작성
        validators = [UniqueValidator(queryset=User.objects.all())] 
        # 겹치는 유저 이메일이 있는지 검증(이메일 중복 방지를 위한 검증 도구)
    )
    password = serializers.CharField(
        required = True,
        write_only = True, # 역직렬화(J->P)만 가능. 직렬화(P->J) 불가능
        validators = [validate_password] # 패스워드가 짧거나 쉽지 않은지 검증(장고의 기본 패스워드 검증 도구)
    )
    re_password = serializers.CharField(required = True, write_only = True)

    class Meta:
        model = User
        fields = ['username', 'password', 're_password', 'email']
        # 기본 유저모델에 유저네임 필드와 위에서 설정했던 패스워드, 리패스워드, 이메일 필드로 시리얼라이저 데이터(dict) 구성

    def validate(self, data):
        if data['password'] != data['re_password']: # 비밀번호가 일치 하지 않으면 에러발생
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
