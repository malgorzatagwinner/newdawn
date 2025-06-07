# documents/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from docs.views import DocumentViewSet, DocumentListView

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),  # This gives you /documents/, /documents/<id>/, etc.
    path('my-documents/', DocumentListView.as_view(), name='my-documents'),  # Optional
]

