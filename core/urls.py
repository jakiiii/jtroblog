import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

from ckeditor_uploader.views import upload, browse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('apps.about.urls', namespace='about')),
    path('contact/', include('apps.contact.urls', namespace='contact')),
    path('', include('apps.blog.urls', namespace='blog')),

    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', login_required(upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(browse)), name='ckeditor_browse'),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
