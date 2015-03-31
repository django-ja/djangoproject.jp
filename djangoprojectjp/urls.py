from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from mezzanine.conf import settings

from djangoja import views

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = i18n_patterns(
    "",
    ("^admin/", include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url("^$", views.top, name="home"),

    # For backward compatibility
    url("^%s/feeds/latest/" % settings.BLOG_SLUG.rstrip("/"),
        views.LatestRSSRedirectView.as_view()),

    ("^", include("mezzanine.urls")),
)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
