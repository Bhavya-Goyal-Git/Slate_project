from django.urls import path
from .views import SignupView, LoginView, StudentAchievementView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("student/achievements/<int:student_id>/", StudentAchievementView.as_view(), name="student_achievement"),
]
