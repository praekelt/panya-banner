from django.contrib import admin

from content.admin import ModelBaseAdmin

from banner.models import CodeBanner, ImageBanner
    

admin.site.register(CodeBanner, ModelBaseAdmin)
admin.site.register(ImageBanner, ModelBaseAdmin)