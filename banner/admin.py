from django import forms
from django.conf import settings
from django.contrib import admin

from banner.models import BannerOption, BannerOptions, CodeBanner, ImageBanner 
from panya.admin import ModelBaseAdmin

def build_url_names(url_patterns=None):
    """
    Returns a tuple of url pattern names suitable for use as field choices
    """
    if not url_patterns:
        urlconf = settings.ROOT_URLCONF
        url_patterns = __import__(settings.ROOT_URLCONF, globals(), locals(), ['urlpatterns', ], -1).urlpatterns
        
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

def build_positions():
    gizmos = __import__(settings.ROOT_GIZMOCONF, globals(), locals(), ['gizmos']).gizmos
    
    slot_names = set()
    for gizmo in gizmos:
        slot_names.add(gizmo[2])
       
    return [(slot_name, slot_name.replace('_', ' ').title()) for slot_name in slot_names]

class BannerOptionAdminForm(forms.ModelForm):
    url_name = forms.ChoiceField(label='URL Name',)
    position = forms.ChoiceField(label='Position',)
    class Meta:
        model = BannerOption

    def __init__(self, *args, **kwargs):
        """
        Set url_name choices to url pattern names
        """
        url_names = build_url_names()
        positions = build_positions()
        self.declared_fields['url_name'].choices = [('', '---------'),] + url_names
        self.declared_fields['position'].choices = [('', '---------'),] + positions
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
