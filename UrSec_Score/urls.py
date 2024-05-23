from django.conf import settings
from django.urls import path, re_path
from profile.views import login_page
from reports.views import index, report, test
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    re_path(r'^report', report, name="reports"),
    re_path(r'^login', login_page, name="login"),
    path("test/", test),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)