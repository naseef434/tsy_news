from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.storage import staticfiles_storage
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('viewers.urls')),
    path('writer/',include('editors.urls')),
    path(
        "ads.txt",
        RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    ),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)