from django import forms
from .models import ApplicationTemplate, ApplicationSubmission, Color, CategoryTag, Question

class ApplicationTemplateForm(forms.ModelForm):

    class Meta:
        model = ApplicationTemplate
        exclude = ['accepted_registrations']

    
class AddQuestionForm(forms.Form):

    question1 = forms.CharField(widget=forms.Textarea)
    question2 = forms.CharField(widget=forms.Textarea, required=False)
    question3 = forms.CharField(widget=forms.Textarea, required=False)
    

