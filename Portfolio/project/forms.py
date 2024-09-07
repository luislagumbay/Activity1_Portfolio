from django import forms
from .models import Inquiry
from .models import Project

class ContactForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['full_name', 'email', 'subject', 'message']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'short_description', 'image', 'project_url']
