from django.db import models
from django.contrib.auth.models import User
from .managers import SoftDeleteManager


class BaseModel(models.Model):
    """Modelo base para Soft Delete e auditoria"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # Managers
    objects = SoftDeleteManager()   # retorna só ativos
    all_objects = models.Manager()  # retorna todos (inclusive deletados)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """Soft delete"""
        self.is_active = False
        self.save()


class UserProfile(BaseModel):
    """Perfil extra do usuário"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    height = models.FloatField(help_text="Altura em metros")
    weight = models.FloatField(help_text="Peso em kg")
    goal = models.CharField(max_length=100, help_text="Ex: Ganho de massa, emagrecimento")

    def __str__(self):
        return f"{self.user.username} - {self.goal}"


class WorkoutPlan(BaseModel):
    """Plano de treino"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout_plans")
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_weeks = models.PositiveIntegerField(default=4, help_text="Duração em semanas")

    def __str__(self):
        return f"Treino {self.name} ({self.user.username})"


class DietPlan(BaseModel):
    """Plano alimentar"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="diet_plans")
    name = models.CharField(max_length=100)
    calories_per_day = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Dieta {self.name} ({self.user.username})"
