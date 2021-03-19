from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, TodoViewSet2, TodoViewSetComplete
router = DefaultRouter()
router.register(r'todos-list', TodoViewSet, basename='user')
router.register(r'todos-cre-del-patch-get', TodoViewSet2, basename='get')
router.register(r'todos/complete', TodoViewSetComplete, basename='complete')

urlpatterns = router.urls



