from inspect import cleandoc
from django import forms
from .models import User
from django.contrib.auth.hashers import make_password, check_password

class RegisterForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': '이메일을 입력해주세요'
    }, max_length=64, label='이메일')
    password = forms.CharField(error_messages={
        'required': '비밀번호를 입력해주세요'
    }, widget=forms.PasswordInput, label='비밀번호')
    re_password = forms.CharField(error_messages={
        'required': '비밀번호를 한번 더 입력해주세요'
    },
    widget=forms.PasswordInput, label='비밀번호 확인')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        password = cleaned_data['password']
        re_password = cleaned_data['re_password']

        if password != re_password:
            self.add_error('password', '비밀번호가 정확하지 않습니다.')
            self.add_error('re_password', '비밀번호가 정확하지 않습니다.')
        else:
            user = User(
                email = email,
                password = make_password(password)
            )

            user.save()

class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': '이메일을 입력해주세요'
    }, max_length=64, label='이메일')
    password = forms.CharField(error_messages={
        'required': '비밀번호를 입력해주세요'
    }, widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('email', '존재하지 않는 이메일입니다')
                return
            if not check_password(password ,user.password):
                self.add_error('password', '비밀번호가 일치하지 않습니다')
            else:
                # 요청한 폼의 이메일 칸의 해당 유저의 이메일을 저장
                self.email = user.email
