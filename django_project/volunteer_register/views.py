from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import ApplicationTemplate, ApplicationSubmission, Question, Answer
from .forms import ApplicationTemplateForm, AddQuestionForm

def index(request):
    all_templates = ApplicationTemplate.objects.all()
    context = {'all_templates': all_templates}
    return render(request, 'volunteer_register/index.html', context)

def register(request):
    return HttpResponse("Hello, volunteers. You're at the registration index.")

def template_detail(request, template_id):
    template = ApplicationTemplate.objects.get(pk=template_id)
    questions = Question.objects.filter(application_template_id=template_id)
    html_questions = "<br>".join([question.question_text for question in questions])
    return HttpResponse(f"This is the detail view for the <b>{template}</b> template. Questions:<br>{html_questions}")

def submission_detail(request, submission_id):
    submission = ApplicationSubmission.objects.get(pk=submission_id)
    questions = Question.objects.filter(application_template_id=submission.application_template).filter(answer__application_submission_id=submission_id)
    answers = Answer.objects.filter(application_submission_id=submission_id)
    qa = zip(questions, answers)
    html_qa = "<br>".join([f'{question.question_text}: {answer.answer_text}' for question, answer in qa])
    return HttpResponse(f"This is the detail view for the application started on <b>{submission.start_date}</b>. Questions, answers:<br>{html_qa}")

def all_templates(request):
    template_list = ApplicationTemplate.objects.all()
    html_template_list = "<br>".join([template.subject for template in template_list])
    return HttpResponse(f"This is the categorical view for all application templates:<br><b>{html_template_list}</b>")

def new_template(request):
    if request.method == 'POST':
        info_form = ApplicationTemplateForm(request.POST, request.FILES)
        question_form = AddQuestionForm(request.POST)
        if info_form.is_valid() and question_form.is_valid():
            new_app_template = info_form.save()
            for question_field_text in question_form.cleaned_data.values():
                if question_field_text != '':
                    new_question = Question(application_template=new_app_template, question_text=question_field_text).save()
            messages.success(request, f'Your new application template has been created.')
            return redirect('index')
    else:
        info_form = ApplicationTemplateForm()
        question_form = AddQuestionForm()

    return render(request, 'volunteer_register/new_applicationtemplate.html', {'info_form': info_form, 'question_form': question_form})

