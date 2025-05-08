from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from docs.views import DocumentViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

