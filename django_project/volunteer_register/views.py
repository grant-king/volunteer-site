from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, volunteers. You're at the home page.")

def register(request):
    return HttpResponse("Hello, volunteers. You're at the registration index.")

def template_detail(request, template_id):
    return HttpResponse(f"This is the detail view for template {template_id}.")

def submission_detail(request, submission_id):
    return HttpResponse(f"This is the detail view for application {submission_id}.")

def all_templates(request):
    return HttpResponse(f"This is the categorical view for all application templates.")
    