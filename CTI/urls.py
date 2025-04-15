from ninja import NinjaAPI
from CTI_APP.api import router as cti_router

from django.contrib import admin
from django.urls import path, include


api = NinjaAPI()

api.add_router("/cti/", cti_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CTI_APP.urls')),
    path('api/', api.urls, name='api'),
]
