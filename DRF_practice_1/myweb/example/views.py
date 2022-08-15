from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BooksAPIGenerics(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'bid'

# class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin ,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'bid'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# @api_view(['GET']) # API 테스트
# def HelloAPI(request):
#     return Response("hello World!")

# @api_view(['GET', 'POST'])
# def booksAPI(request):
#     if request.method == 'GET': # 도서 전체 정보
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         # 데이터(모델 인스턴스)가 1개 이상이므로 전체 데이터를 한번에 직렬화(P->J)하도록 many=True 옵션 적용
#         return Response(serializer.data, status=status.HTTP_200_OK) # 가공된 데이터와 상태코드 전송
#     elif request.method == 'POST': # 도서 정보 등록
#         serializer = BookSerializer(data=request.data) # 요청한 데이터를 역직렬화(J->P)
#         if serializer.is_valid(): # 모델에 맞는 유효한 데이터라면
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) # 가공된 데이터와 상태코드 전송
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST) # 에러 메세지와 상태코드 전송

# @api_view(['GET'])
# def bookAPI(request, bid):
#     book = get_object_or_404(Book, bid=bid) # 요청 bid와 맞는 Book 객체가 존재하면 가져오고 없으면 404
#     serializer = BookSerializer(book) # 데이터 직렬화(P->J)
#     return Response(serializer.data, status=status.HTTP_200_OK) # 가공된 데이터와 상태코드 전송