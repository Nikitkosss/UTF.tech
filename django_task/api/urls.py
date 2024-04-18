from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodCategoryViewSet

router = DefaultRouter()
router.register(r'foods', FoodCategoryViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
