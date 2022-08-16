from rest_framework import status, generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Todo
from .serializers import TodoCreateSerializer, TodoDetailSerializer, TodoSimpleSerializer

# Create your views here.

# 완료하지 못한 투두 조회
# Viewset
# 필터기능, 투두 완료 기능 시도
class TodosAPIViewsets(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSimpleSerializer
# Generics
class TodosAPIGenerics(generics.ListAPIView):
    queryset = Todo.objects.filter(complete=False)
    serializer_class = TodoSimpleSerializer
# Mixins
class TodosAPIMixins(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.filter(complete=False)
    serializer_class = TodoSimpleSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
# APIView
class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete=False) # 미완료된 투두객체만 가져오기
        serializer = TodoSimpleSerializer(todos, many=True) # 직렬화(P->J), 데이터가 하나 이상이므로 many 옵션
        return Response(serializer.data, status=status.HTTP_200_OK) # 직럴화 한 데이터와 상태코드 전송

    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data) # 역직렬화(J->P), 요청에서 보낸 데이터를 가공
        if serializer.is_valid(): # 유효한 데이터라면
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 역직렬화 한 데이터와 상태코드 전송
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 투두 상세 조회 및 수정
# Generics
class TodoAPIGenerics(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer
    lookup_field = 'pk'
# Mixins
class TodoAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin ,generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs): # method
        return self.retrieve(request, *args, **kwargs) # 해당 method로 요청이 왔을 때 처리
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
# APIView
class TodoAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk) # 투두객체에 id가 pk인 값이 있으면 가져오고 없으면 404
        serializer = TodoDetailSerializer(todo) # 직렬화(p->J)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 완료한 투두 조회
# Generics
class DoneTodosAPIGenerics(generics.ListAPIView):
    queryset = Todo.objects.filter(complete=True)
    serializer_class = TodoSimpleSerializer
# Mixins
class DoneTodosAPIMixins(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.filter(complete=True)
    serializer_class = TodoSimpleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
# APIView
class DoneTodosAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodoSimpleSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 완료한 투두로 설정 
# Generics
# 투두 완료 기능 시도
# class DoneTodoAPIGenerics(generics.RetrieveAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoDetailSerializer
#     lookup_fleid = 'pk'

# Mixins
class DoneTodoAPIMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    lookup_fleid = 'pk'

    def retrieve(self, request, *args, **kwargs): # 기존의 retrieve 함수를 변형
        instance = self.get_object() # id 값으로 객체 탐색
        return instance # 객체 반환
    
    def get(self, request, *args, **kwargs):
        todo = self.retrieve(request, *args, **kwargs) # 반환 된 객체 저장
        todo.complete = True # 객체를 완료 처리
        todo.save() # 저장
        return Response(status=status.HTTP_200_OK) # 상태코드 전송

# APIView
class DoneTodoAPIView(APIView):
    def get(self, request, pk):
        done = get_object_or_404(Todo, id=pk)
        done.complete = True
        done.save()
        return Response(status=status.HTTP_200_OK)