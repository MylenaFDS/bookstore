"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import debug_toolbar
from bookstore import views
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    path("bookstore/<str:version>/pedido/", include("order.urls"), name="lista_de_pedidos"),
    path("bookstore/<str:version>/order/<str:pk>/", views.order_detail, name="order-detail"),
    path("bookstore/<str:version>/produto/", include("product.urls"), name="lista_de_produtos"),
    path("bookstore/<str:version>/produto/<str:pk>/", views.product_detail, name="detalhe_do_produto"),
    path("bookstore/<str:version>/categoria/", views.category_list, name="lista_de_categorias"),
    path("bookstore/<str:version>/categoria/<str:pk>/", views.category_detail, name="categoria-detalhe"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("update_server/", views.update, name="update"),
    path('', views.hello_world, name='home'),
]

