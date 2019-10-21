from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TextQuestion(models.Model):
    title = models.TextField()
    status = models.CharField(default='inactive', max_length=10)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.textchoice_set.all()


class TextChoice(models.Model):
    question = models.ForeignKey('survey.TextQuestion', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __self__(self):
        return self.text

    @property
    def votes(self):
        return self.textanswer_set.count()


class TextAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(TextChoice, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.choice.text)
