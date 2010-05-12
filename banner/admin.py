from django import forms
from django.conf import settings
from django.contrib import admin

from banner.models import BannerOption, BannerOptions, CodeBanner, ImageBanner 
from content.admin import ModelBaseAdmin

def build_url_names(url_patterns):
    """
    Returns a tuple of url pattern names suitable for use in field choices
    """
    result = []
    for pattern in url_patterns:
        try:
            result.append((pattern.name, pattern.name.title().replace('_', ' ')))
        except AttributeError:
            # if the pattern itself is an include, recurively fetch it patterns.
            # ignore admin patterns
            if not pattern.regex.pattern.startswith('^admin'):
                try:
                    result += build_url_names(pattern.url_patterns)
                except AttributeError:
                    pass
    return result

class BannerOptionAdminForm(forms.ModelForm):
    url_name = forms.ChoiceField(choices=(('1','1'),))
    class Meta:
        model = BannerOption

    def __init__(self, *args, **kwargs):
        """
        Set url_name choices to url pattern names
        """
        urlconf = settings.ROOT_URLCONF
        url_patterns = __import__(settings.ROOT_URLCONF, globals(), locals(), ['urlpatterns', ], -1).urlpatterns
        url_names = build_url_names(url_patterns)
        self.declared_fields['url_name'].choices = url_names
        super(BannerOptionAdminForm, self).__init__(*args, **kwargs)
    
class BannerOptionInline(admin.TabularInline):
    form = BannerOptionAdminForm
    model = BannerOption

class BannerOptionsAdmin(admin.ModelAdmin):
    inlines = [
        BannerOptionInline,
    ]
    

admin.site.register(BannerOptions, BannerOptionsAdmin)
admin.site.register(CodeBanner, ModelBaseAdmin)
admin.site.register(ImageBanner, ModelBaseAdmin)
