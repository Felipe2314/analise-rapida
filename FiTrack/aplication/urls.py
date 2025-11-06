# aplication/urls.py
# aplication/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, WorkoutPlanViewSet, DietPlanViewSet

# Crie um router
router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile')
router.register(r'workoutplans', WorkoutPlanViewSet, basename='workoutplan')
router.register(r'dietplans', DietPlanViewSet, basename='dietplan')

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path




#urlpatterns = [
   # path('api/v1', include('aplication.urls')), #v1
   # path('api/v2', include('aplication.urls')), #novas versoes
#]

