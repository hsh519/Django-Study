from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class Loginform(forms.Form):
    # 값 변경/검사 및 html 코드에 랜더링할 데이터 설정
    username = forms.CharField(
        error_messages={
            # 상황별 에러메세지 설정
            'required': '아이디를 입력해주세요.'
        },
        max_length=32, label='사용자 이름')
    password = forms.CharField(
        error_messages={
            # 상황별 에러메세지 설정 
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username') # username 필드에 있는 값 가져오기
        password = cleaned_data.get('password') # password 필드에 있는 값 가져오기

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist: # 없는 유저일 경우 예외처리
                self.add_error('username','존재하지 않는 유저입니다')
                return
            if not check_password(password, user.password): 
                self.add_error('password', '비밀번호를 틀렸습니다') 
            else: 
                self.user_id = user.id