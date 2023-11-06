from django.db import models

# Create your models here.

class CustomForm(models.Model):
    questions = models.TextField()
    fields    = models.TextField()

    def get_questions(self):
        return self.questions.split('&')

    def get_fields(self):
        return self.fields.split('&')

class Responds(models.Model):
    name      = models.CharField(max_length = 60)
    surname   = models.CharField(max_length = 60)
    num       = models.IntegerField()
    
    form      = models.ForeignKey(CustomForm, on_delete=models.CASCADE)
    responses = models.TextField()