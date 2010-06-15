import unittest

from django.conf import settings
from django.conf.urls.defaults import patterns, url
from django.contrib.sites.models import Site

from banner.templatetags import banner_inclusion_tags
from banner.models import Banner, BannerOption
from preferences import preferences

urlpatterns = patterns(
    '',
    url(r'^some/path$', object, name='test_view_name'),
    url(r'^no/specified/banners$', object, name='no_specified_banners'),
)

class BannerInclusionTagsTestCase(unittest.TestCase):

    def test_resolve_banner(self):
        # create dummy request object
        request = type('Request', (object,), {})
        request.urlconf = 'banner.tests'
        request.path = '/some/path'

        # setup unpublished banner
        unpublished_banner = Banner()
        unpublished_banner.save()

        # setup banneroption
        option = BannerOption(banner=unpublished_banner, banner_preferences=preferences.BannerPreferences, url_name="test_view_name", position="header")
        option.save()

        # unpublished banners should not be returned
        self.failIfEqual(unpublished_banner, banner_inclusion_tags.resolve_banner(request, 'header'))
        
        # setup published banner
        web_site = Site(domain="web.address.com")
        web_site.save()
        settings.SITE_ID = web_site.id
        published_banner = Banner(state="published")
        published_banner.save()
        published_banner.sites.add(web_site)

        # setup banneroption
        option = BannerOption(banner=published_banner, banner_preferences=preferences.BannerPreferences, url_name="test_view_name", position="header")
        option.save()

        # published banners should be returned
        self.failUnlessEqual(published_banner, banner_inclusion_tags.resolve_banner(request, 'header'))

        # banner should not be returned of its position does not correspond to a gizmo slot 
        self.failIfEqual(published_banner, banner_inclusion_tags.resolve_banner(request, 'bogus slot'))
        
        # setup another published banner
        web_site = Site(domain="web.address.com")
        web_site.save()
        settings.SITE_ID = web_site.id
        published_banner2 = Banner(state="published")
        published_banner2.save()
        published_banner2.sites.add(web_site)

        # setup banneroption by url
        option = BannerOption(banner=published_banner2, banner_preferences=preferences.BannerPreferences, url_name="test_view_name", url="/some/path", position="header")
        option.save()
        # banner with url specified takes priority 
        self.failIfEqual(published_banner2, banner_inclusion_tags.resolve_banner(request, 'header'))

        # setup another published banner
        web_site = Site(domain="web.address.com")
        web_site.save()
        settings.SITE_ID = web_site.id
        published_banner3 = Banner(state="published")
        published_banner3.save()
        published_banner3.sites.add(web_site)
        
        # setup banneroption
        option = BannerOption(banner=published_banner3, banner_preferences=preferences.BannerPreferences, url_name="test_view_name", position="header", is_default=True)
        option.save()
        
        # in case no banner is found directly, fall back to default for gizmo slot
        request.path='/no/specified/banners'
        self.failUnlessEqual(published_banner3, banner_inclusion_tags.resolve_banner(request, 'header'))
