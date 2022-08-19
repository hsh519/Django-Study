from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import LoginSerializer, ProfileSerializer, RegisterSerializer
from .models import Profile

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data) # 요청에서 보낸 데이터 역직렬화
        serializer.is_valid(raise_exception=True)
        # validate 함수로 유효성 검사 유효하면 token, 그렇지 않으면 error 리턴
        token = serializer.validated_data # 유효성 검사 후 리턴 된 데이터 저장(token)
        return Response({"token": token.key}, status=status.HTTP_200_OK) # 토큰 객체의 키와 상태코드 전송

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
