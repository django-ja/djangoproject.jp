from django.views.generic import RedirectView

from mezzanine.core.views import direct_to_template


def top(request):
    return direct_to_template(request, template="index.html")


class LatestRSSRedirectView(RedirectView):
    """ Redirect latest => RSS feed for compatible from zinnia.
    """
    permanent = False
    pattern_name = "blog_post_feed"

    def get_redirect_url(self, *args, **kwargs):
        return super(LatestRSSRedirectView, self).get_redirect_url('rss')
