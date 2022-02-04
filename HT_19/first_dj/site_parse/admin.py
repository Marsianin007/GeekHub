from django.contrib import admin
from .models import AskModel, ShowModel, JobModel, NewsModel


admin.site.register(AskModel)
admin.site.register(ShowModel)
admin.site.register(JobModel)
admin.site.register(NewsModel)