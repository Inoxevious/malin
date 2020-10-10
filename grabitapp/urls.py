"""grabitapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from pages.views import index
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
router = DefaultRouter()
urlpatterns = [
    path('', index, name='index'),
    path('pages/', include('pages.urls')),
    path('account/', include('account.urls')),
    path('individual/', include('individual.urls')),
    path('ecommerce_app/', include('ecommerce_app.urls')),
    path('mush_store/', include('mush_store.urls')),
    path('search/', include('search.urls')),
    path('o/', include('oauth2_provider.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('', TemplateView.as_view(template_name='index.html', extra_context={
        "instagram_profile_name": "malin_collection"
    })),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)