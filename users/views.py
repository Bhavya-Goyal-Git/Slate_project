from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import SignupSerializer, StudentAchievementSerializer
from rest_framework.permissions import IsAuthenticated
from .models import StudentAchievement

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"id": user.id, "email": user.email, "name": user.name, "role": user.role},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                },
                status=status.HTTP_200_OK
            )
        return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)


class StudentAchievementView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        if request.user.role not in ["student", "parent"]:
            return Response({"error": "Access denied"}, status=status.HTTP_403_FORBIDDEN)

        try:
            achievement = StudentAchievement.objects.get(id=student_id)
            if request.user.student_achievement.id != achievement.id:
                return Response({"error": "You can only access your achievement data."}, status=status.HTTP_403_FORBIDDEN)
            
            serializer = StudentAchievementSerializer(achievement)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except StudentAchievement.DoesNotExist:
            return Response({"error": "Student Achievement not found"}, status=status.HTTP_404_NOT_FOUND)