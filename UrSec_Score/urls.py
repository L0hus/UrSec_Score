from django.conf import settings
from django.urls import path, re_path
from User import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index),
    re_path(r'^report', views.report),
    path("test/", views.test),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)