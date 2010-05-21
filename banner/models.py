from django.db import models

from content.models import ModelBase
from options.models import Options

class Banner(ModelBase):
    pass

class CodeBanner(Banner):
    code = models.TextField(
        help_text='The full HTML/Javascript code snippet to be embedded for this banner.'
    )
    
    class Meta():
        verbose_name = 'Code banner'
        verbose_name_plural = 'Code banners'

class ImageBanner(Banner):
    url = models.CharField(
        max_length='256', 
        verbose_name='URL', 
        help_text='URL (internal or external) to which this banner will link.'
    )
    
    class Meta():
        verbose_name = 'Image banner'
        verbose_name_plural = 'Image banners'

    def get_absolute_url(self):
        return self.url

class BannerOptions(Options):
    __module__ = 'options.models'

    class Meta():
        verbose_name = 'Banner options'
        verbose_name_plural = 'Banner options'

class BannerOption(models.Model):
    banner_options = models.ForeignKey('options.BannerOptions')
    is_default = models.BooleanField(
        verbose_name="Default",
        default=False,
    )
    url_name = models.CharField(
        max_length=256,
        verbose_name="URL Name",
        blank=True,
        null=True,
    )
    url = models.CharField(
        max_length=256,
        verbose_name="URL (takes precedence)",
        blank=True,
        null=True,
    )
    banner = models.ForeignKey('banner.Banner')
    position = models.CharField(max_length=256)
