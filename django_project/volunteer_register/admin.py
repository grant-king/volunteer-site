from django.contrib import admin

from .models import ApplicationTemplate, ApplicationSubmission, Question, Choice, Answer

admin.site.register(ApplicationTemplate)
admin.site.register(ApplicationSubmission)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Choice)
