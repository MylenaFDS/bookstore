from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
import debug_toolbar
from django.http import HttpResponse


urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),

    # --- API real usada nos testes ---
    path("api/", include("product.urls")),
    path("api/", include("order.urls")),

    # Auth token
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),

    # Página simples
    path('', lambda request: HttpResponse("API Bookstore OK")),
]
