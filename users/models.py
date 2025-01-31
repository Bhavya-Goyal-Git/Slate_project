from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, role=None):
        if not email:
            raise ValueError("Users must have an email address")
        if role not in ["school", "student", "parent"]:
            raise ValueError("Role must be one of: school, student, parent")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password, role="school")
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class StudentAchievement(models.Model):
    name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    achievements = models.TextField()

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ("school", "School"),
        ("student", "Student"),
        ("parent", "Parent"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    student_achievement = models.ForeignKey(
        StudentAchievement, 
        on_delete=models.CASCADE, 
        null=True, blank=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "role"]

    def __str__(self):
        return self.email