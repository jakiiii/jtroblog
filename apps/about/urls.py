from django.urls import path
from apps.about.views import AboutView


app_name = 'about'


urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]
