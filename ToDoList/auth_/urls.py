from django.urls import re_path, include

from .views import RegistrationAPIView, LoginAPIView



from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'login', LoginAPIView, basename='login')
router.register(r'registration', RegistrationAPIView, basename='registration')

urlpatterns = router.urls



