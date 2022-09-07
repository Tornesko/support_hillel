from django.urls import path, include, re_path
from rest_framework_simplejwt import views

urlpatterns = [
    # path("token/", views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("token/refresh/", views.TokenRefreshView.as_view(), name="token_refresh"),
    # path("token/verify/", views.TokenVerifyView.as_view(), name="token_verify"),
    path('auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
