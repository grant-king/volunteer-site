from django import forms
from .models import ApplicationTemplate, ApplicationSubmission, Color, CategoryTag

class ApplicationTemplateForm(forms.ModelForm):
    subject = forms.CharField(label='Subject')
    organization = forms.CharField(label='Your Organization')
    assignment = forms.CharField(label='Assignment')
    job_description = forms.CharField(label='Job Description', widget=forms.Textarea)
    image = forms.ImageField(label='Listing Image')
    background_color = forms.ModelChoiceField(queryset=Color.objects.all())
    category_tags = forms.ModelMultipleChoiceField(queryset=CategoryTag.objects.all())
    max_registrations = forms.IntegerField(label='Max Registrations')

    class Meta:
        model = ApplicationTemplate
        fields = ['subject', 'organization', 'assignment', 'job_description', 'image', 'background_color', 'category_tags', 'max_registrations']
