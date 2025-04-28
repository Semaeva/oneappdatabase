from ninja import NinjaAPI
from CTI_APP.api import router as cti_router
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from django.contrib import admin
from django.urls import path, include
from ninja.security import HttpBearer
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


api = NinjaExtraAPI(
   title="API",
   description="Документация API",
    version="1.0",
    docs_decorator=login_required,
    auth=GlobalAuth()
)
# https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/

api.register_controllers(NinjaJWTDefaultController)


api.add_router("/cti/", cti_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CTI_APP.urls')),
    path('api/', api.urls, name='api'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()