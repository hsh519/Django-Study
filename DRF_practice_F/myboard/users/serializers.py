from django.contrib.auth.models import User # 기본 유저 모델
from django.contrib.auth.password_validation import validate_password # 장고의 기본 패스워드 검증 도구
from django.contrib.auth import authenticate # User 인증 함수

from rest_framework import serializers # 시리얼라이저
from rest_framework.authtoken.models import Token # 토큰 모델
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구

from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True, # 무조건 작성
        validators = [UniqueValidator(queryset=User.objects.all())] 
        # 겹치는 유저 이메일이 있는지 검증(이메일 중복 방지를 위한 검증 도구)
    )
    password = serializers.CharField(
        required = True,
        write_only = True, 
        # 역직렬화(J->P)만 가능. 직렬화(P->J) 불가능.
        # 패스워드 사용자 검증에만 사용하기 떄문에 굳이 작렬화해 전달할 이유가 없음
        validators = [validate_password] # 패스워드가 짧거나 쉽지 않은지 검증(장고의 기본 패스워드 검증 도구)
    )
    re_password = serializers.CharField(required = True, write_only = True)

    class Meta:
        model = User
        fields = ['username', 'password', 're_password', 'email']
        # 기본 유저모델에 유저네임 필드와 위에서 설정했던 패스워드, 리패스워드, 이메일 필드로 시리얼라이저 데이터(dict) 구성

    def validate(self, data): # object 에 대한 validator 직접 구현(패스워드 확인)
        if data['password'] != data['re_password']: # 비밀번호가 일치 하지 않으면 에러발생
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return data

    def create(self, validated_data): # 유효성 검사를 다 했다면 유저 등록
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user) # 유저 별 토큰 생성
        return user

class LoginSerializer(serializers.Serializer): 
    # 로그인은 사용자 정보를 확인하는 절차이기 떄문에 굳이 모델이 필요가 없음
    username = serializers.CharField(
        required = True
    )
    password = serializers.CharField(
        required = True,
        write_only = True
    )

    def validate(self, data):
        # 자격증명(data)을 인자로 받아 자격증명이 유효하면 User 객체, 그렇지 않으면 None
        # 사용자가 해당 아이디를 사용할 자격이 되는지 확인하는 과정이 자격증명.
        # 따라서 id와 password를 인자로 받아 증명함
        # data의 개수가 정해져있지 않으므로 **로 여러개의 인수를 받을 것임을 나타냄
        user = authenticate(**data)
        if user: # 유저가 있다면
            token = Token.objects.get(user=user) # 해당 유저의 토큰을 가져와 응답
            return token
        raise serializers.ValidationError(
            {"error": "로그인에 실패했습니다."}
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nickname', 'position', 'subjects', 'image']

    