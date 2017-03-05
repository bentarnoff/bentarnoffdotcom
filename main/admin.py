from django.contrib import admin
import models

admin.site.register(models.BlogPost)
admin.site.register(models.Article)
admin.site.register(models.Interview_video)
admin.site.register(models.Interview_audio)
admin.site.register(models.Interview_text)