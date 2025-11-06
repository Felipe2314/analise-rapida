# Importe a função 'render' aqui
from django.shortcuts import render
from django.http import HttpResponse # Importe também HttpResponse, se for usar em outras views

def home_page(request):
    """
    Renderiza a página inicial.
    """
    return render(request, 'aplication/index.html')

# O restante do seu código vem aqui, como os ViewSets
from rest_framework import viewsets
from .models import UserProfile, WorkoutPlan, DietPlan
from .serializers import UserProfileSerializer, WorkoutPlanSerializer, DietPlanSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API para visualizar, criar, atualizar e deletar perfis de usuários.
    """
    serializer_class = UserProfileSerializer
    
    def get_queryset(self):
        """
        Garante que um usuário só possa ver e editar seu próprio perfil.
        """
        user = self.request.user
        if user.is_authenticated:
            # Filtra o queryset para retornar apenas o perfil do usuário logado.
            # Usa o .all_objects para lidar com o soft delete, caso necessário.
            return UserProfile.all_objects.filter(user=user)
        # Retorna um queryset vazio se o usuário não estiver autenticado.
        return UserProfile.objects.none()


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar planos de treino.
    """
    serializer_class = WorkoutPlanSerializer
    
    def get_queryset(self):
        """
        Permite que um usuário gerencie apenas seus próprios planos de treino.
        """
        user = self.request.user
        if user.is_authenticated:
            # Retorna apenas os planos de treino associados ao usuário logado.
            return WorkoutPlan.objects.filter(user=user)
        return WorkoutPlan.objects.none()


class DietPlanViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar planos alimentares.
    """
    serializer_class = DietPlanSerializer
    
    def get_queryset(self):
        """
        Permite que um usuário gerencie apenas seus próprios planos alimentares.
        """
        user = self.request.user
        if user.is_authenticated:
            # Retorna apenas os planos de dieta associados ao usuário logado.
            return DietPlan.objects.filter(user=user)
        return DietPlan.objects.none()