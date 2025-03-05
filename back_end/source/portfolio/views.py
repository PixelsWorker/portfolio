from django.views.generic import TemplateView, DetailView
from .models import SkillCard, WorkExperience, Project, Footer, SocialLink
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def truncate_description(text, word_limit=50):
    """Utility function to trim a description to a given number of words."""
    words = text.split()
    if len(words) > word_limit:
        return " ".join(words[:word_limit]) + "..."
    return text

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include all models for home page
        context['skill_cards'] = SkillCard.objects.all()
        context['work_experiences'] = WorkExperience.objects.all()
        projects = Project.objects.all()
        # Attach a short version of description to each project
        for project in projects:
            project.short_desc = truncate_description(project.description)
        context['projects'] = projects
        context['footer'] = Footer.objects.first()
        context['social_links'] = SocialLink.objects.all()
        return context

class ProjectsView(TemplateView):
    template_name = 'projects_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        for project in projects:
            project.short_desc = truncate_description(project.description)
        context['projects'] = projects
        context['footer'] = Footer.objects.first()
        context['social_links'] = SocialLink.objects.all()
        return context

# DetailView for a single project (using the slug)
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer'] = Footer.objects.first()
        context['social_links'] = SocialLink.objects.all()
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer'] = Footer.objects.first()
        context['social_links'] = SocialLink.objects.all()
        return context





