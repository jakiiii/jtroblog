import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from django.conf.urls.static import static
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

from apps.blog.sitemaps import PostSitemap
from ckeditor_uploader.views import upload, browse

sitemaps = {
    'posts': PostSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('apps.about.urls', namespace='about')),
    path('contact/', include('apps.contact.urls', namespace='contact')),
    path('', include('apps.category.urls', namespace='category')),
    path('', include('apps.blog.urls', namespace='blog')),

    path('ckeditor/upload/', login_required(upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(browse)), name='ckeditor_browse'),

    # sitemaps
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
