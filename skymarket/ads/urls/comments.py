from django.urls import include, path
from rest_framework_nested import routers

from ads.views import AdViewSet, CommentViewSet

comment_router = routers.SimpleRouter()
comment_router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path('', include(comment_router.urls)),
]
