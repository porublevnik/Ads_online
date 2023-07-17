from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("api/", include("users.urls")),
    path("api/", include("ads.urls.ads")),
    path("api/", include("ads.urls.comments")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)