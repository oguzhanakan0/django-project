from django.contrib import admin

# Register your models here.
from .models import *

# Basic Models
admin.site.register(ClassName)
admin.site.register(ProductCampaign)
admin.site.register(AlertType)
admin.site.register(Result)
admin.site.register(AlertLog)
admin.site.register(ScrapeLog)