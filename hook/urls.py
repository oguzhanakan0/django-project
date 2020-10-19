from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from home import views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

# router = routers.DefaultRouter()
# router.register(r'_users', views.UserViewSet)
# router.register(r'_groups', views.GroupViewSet)

urlpatterns = [
    # path('api/', include(router.urls)), 
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'', include('home.urls')),
    re_path(r'^kredi/', include('loans.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^blog/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
