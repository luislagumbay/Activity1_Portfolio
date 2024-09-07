from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Inquiry
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['title', 'description', 'short_description', 'image', 'project_url']
    template_name = 'portfolio/project_create.html'  # Ensure this matches the filename
    success_url = reverse_lazy('project-list')  # Redirect to the project list after successful creation

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['title', 'description', 'short_description', 'image', 'project_url']
    template_name = 'portfolio/project_update.html'  # Make sure this matches the template name
    success_url = reverse_lazy('project-list')  # Redirect to the project list after update

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')  # Redirect to the project list after deletion
    template_name = 'portfolio/project_confirm_delete.html'  # Template for confirming the deletion

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

@login_required
def dashboard(request):
    inquiries = Inquiry.objects.all()
    return render(request, 'portfolio/dashboard.html', {'inquiries': inquiries})
