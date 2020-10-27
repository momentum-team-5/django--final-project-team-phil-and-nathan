"""snippetSrc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from snippet import views as snippet_views

# from django.contrib import admin
# from django.urls import path, include
# from snippet import views as snippet_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('contact/', snippet_views.contact_us, name='contact_us'),
    path('', snippet_views.snippets_list, name="snippets_list"),
    path('more_information/<int:pk>/', snippet_views.snippets_detail, name="snippets_detail"),
    # path('add/', snippet_views.snippets_add, name="snippets_add"),
    # path('delete/<int:pk>/', snippet_views.snippets_delete, name='snippets_delete'),
    # path('edit/<int:pk>/', snippet_views.snippets_edit, name='snippets_edit'),
    # path('search/', snippet_views.snippets_search, name='snippets_search'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns




