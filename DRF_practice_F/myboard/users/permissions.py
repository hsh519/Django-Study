from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission): 
    # 각 객체에 메소드에 따른 권한 부여. 따라서 객체 권한 함수 오버라이딩
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # 데이터에 변화를 주지않는 안전한 메소드라면(GET 이라면)
            return True # True면 권한 통과
        return obj.user == request.user # 수정할 객체와 요청한 객체가 같으면 수정 가능, 다르면 수정 불가