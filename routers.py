from rest_framework.routers import SimpleRouter
from dogs.viewsets import DogViewSet

router = SimpleRouter()
router.register(r'dogs', DogViewSet, basename='dogs')

urlpatterns = router.urls