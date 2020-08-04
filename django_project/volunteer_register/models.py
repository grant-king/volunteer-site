from django.db import models

class Color(models.Model):
    red = models.PositiveSmallIntegerField()
    green = models.PositiveSmallIntegerField()
    blue = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.red}, {self.green}, {self.blue}'


class CategoryTag(models.Model):
    label = models.CharField(max_length=18)

    def __str__(self):
        return f'{self.label}'


class ApplicationTemplate(models.Model):
    subject = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    assignment = models.CharField(max_length=100)
    job_description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='application_pics', blank=True)
    background_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category_tags = models.ManyToManyField(CategoryTag)
    max_registrations = models.IntegerField(default=2)
    accepted_registrations = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.subject}: {self.assignment}'


class ApplicationSubmission(models.Model):
    application_template = models.ForeignKey(ApplicationTemplate, on_delete=models.CASCADE)
    start_date = models.DateTimeField()

    def __str__(self):
        return f'{self.id} - {self.start_date}'

    def save_answers(self):
        pass


class Question(models.Model):
    application_template = models.ForeignKey(ApplicationTemplate, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.application_template.name[:10]} - {self.question_text}'


class Answer(models.Model):
    application_submission = models.ForeignKey(ApplicationSubmission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return f'{self.application_submission.id} - {self.question.question_text[:20]} - {self.answer_text[:30]}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

