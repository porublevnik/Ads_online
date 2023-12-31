from rest_framework import pagination, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Ad, Comment
from .filters import AdFilter
from .serializers import AdSerializer, CommentSerializer

from ads.permissions import AdAdminPermission, IsExecutor, IsOwner


class AdPagination(pagination.PageNumberPagination):
    page_size = 5



class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [IsOwner, ]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated, ]
        elif self.action in ["create", "update", "partial_update", "destroy", "me"]:
            self.permission_classes = [IsAuthenticated, AdAdminPermission | IsExecutor]

        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = None
    permission_classes = [AllowAny]


    def get_permissions(self):
        if self.action == "retrieve":
            self.permission_classes = [IsAuthenticated, ]
        elif self.action in ["create", "update", "partial_update", "destroy", ]:
            self.permission_classes = [IsAuthenticated, AdAdminPermission | IsExecutor]
        return super().get_permissions()

