from django.contrib import admin

from .models import ApplicationTemplate, ApplicationSubmission, Question, Choice, Answer, Color, CategoryTag

admin.site.register(ApplicationTemplate)
admin.site.register(ApplicationSubmission)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Choice)
admin.site.register(Color)
admin.site.register(CategoryTag)
