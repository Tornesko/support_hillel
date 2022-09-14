from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from exchangerates.urls import urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchangerates/", include("exchangerates.urls")),
    path("tickets/", include("core.urls")),
    path("authentication/", include("authentication.urls")),
]
if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
