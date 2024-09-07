from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='project/static/portfolio/images/')
    date_posted = models.DateTimeField(auto_now_add=True)
    project_url = models.URLField(max_length=200, blank=True)
    class Meta:
        app_label = 'project'

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inquiry from {self.full_name} - {self.subject}'