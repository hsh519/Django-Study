from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import Loginform
from .models import User

# Create your views here.

def register(request):
    if(request.method == 'GET'): 
        return render(request, 'register.html')
    elif(request.method == 'POST'): 
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not(username and useremail and password and re_password):
            res_data['error'] = '값을 입력해주세요!'
        elif(password != re_password):
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            user.save()
            return redirect('/')

        return render(request, 'register.html', res_data)

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'GET': # 사이트를 접속했을 때
        form = Loginform() # 로그인 폼 그대로 가져오기
    elif request.method == 'POST': # 로그인 버튼을 클릭했을 때
        form = Loginform(request.POST) # 로그인 폼에 값을 넣어 가져오기
        if form.is_valid(): # 폼에 있는 데이터를 다 입력했다면
            request.session['user'] = form.user_id # 해당 유저 아이디 값을 세션에 저장
            return redirect('/') # 홈페이지로 이동
    return render(request, 'login.html', {'form': form}) # 로그인 폼을 html 에 랜더링

def logout(request):
    if request.session.get('user'): # 세션값이 있다면(=로그인 되어있다면)
        del(request.session['user']) # 세션값 삭제

    return redirect('/')