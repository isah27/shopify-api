from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Shopify API",
      default_version='v1',
      description="A rest API for online shopping service",
      contact=openapi.Contact(email="isahnaziru27@gmail.com"),
      license=openapi.License(name="No license required, It's free.."),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('products/',include('products.urls')),
    path('category/',include('category.urls')),
    path('orders/',include('orders.urls')),
    path('cart/',include('cart.urls')),
    path('ratings/', include('ratings.urls')),
   #  path('auth/', include('djoser.urls.jwt')),
    path('swagger<format>.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
