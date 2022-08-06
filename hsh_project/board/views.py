from django.shortcuts import redirect, render
from django.http import Http404
from django.core.paginator import Paginator
from .models import Board
from .forms import Boardform
from user.models import User

# Create your views here.

def board_list(request):
    all_boards = Board.objects.all().order_by('-id') # 모든 보드 객체를 가져와 아이디 역순으로 나열(최신순)
    page = int(request.GET.get('p', 1)) # p번째 페이지. 디폴트값 1
    paginator = Paginator(all_boards, 2) # 객체를 몇개씩 묶어 보여줄 것인지

    boards = paginator.get_page(page) # 보여줄 페이지
    return render(request, 'board_list.html', {'boards': boards})

def board_write(request):
    if not request.session.get('user'): # 로그인을 안하고 접근할 경우 로그인 페이지로 강제 이동
        return redirect('/user/login')

    if(request.method == 'GET'):
        form = Boardform()
    elif(request.method == 'POST'):
        form = Boardform(request.POST)
        if form.is_valid():
            userid = request.session.get('user')
            user = User.objects.get(pk=userid)

            board = Board() # 모델 객체 생성
            board.title = form.cleaned_data['title'] # cleaned_data 딕셔너리에서 꺼내오기
            board.contents = form.cleaned_data['contents']
            board.writer = user

            board.save()    
            return redirect('/board/list')
    return render(request, 'board_write.html', {'form': form})

def board_detail(request, pk): # pk는 주소로 붙어 받아온다 ex) detail/1
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist: # 404 에러를 가져와 예외 처리
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board': board})