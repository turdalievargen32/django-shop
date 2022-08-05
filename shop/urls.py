from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategotyViewSet, CommentViewSet, ProductViewSet, toggle_like, add_rating

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register('categories', CategotyViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/toggle_like/<int:p_id>/', toggle_like),
    path('products/add_rating/<int:p_id>/', add_rating),
]
