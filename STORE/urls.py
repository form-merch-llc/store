from ariadne.contrib.django.views import GraphQLView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", GraphQLView.as_view(schema=schema), name="graphql"),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns = (
        [path("__debug__/", include(debug_toolbar.urls))]
        + urlpatterns
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
