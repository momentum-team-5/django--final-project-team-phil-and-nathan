from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from snippet import views as snippet_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls'))
    path('', snippet_views.snippet_list, name="snippet_list"),
    path('snippet_detail/<int:pk>/', snippet_views.snippet_detail, name="snippet_detail"),
    path('add/', snippet_views.add_snippet, name="add_snippet"),
    path('delete/<int:pk>/', snippet_views.delete_snippet, name='delete_snippet'),
    path('edit/<int:pk>/', snippet_views.edit_snippet, name='edit_snippet'),
    path('search/', snippet_views.search, name='search_snippet'),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns




