from django.db import models

class ApplicationTemplate(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ApplicationSubmission(models.Model):
    application_template = models.ForeignKey(ApplicationTemplate, on_delete=models.CASCADE)
    start_date = models.DateTimeField()

    def __str__(self):
        return str(self.start_date)

    def save_answers(self):
        pass


class Question(models.Model):
    application_template = models.ForeignKey(ApplicationTemplate, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


