from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Skill cards: Each card has a title and items (for simplicity, a comma-separated list of tools)
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SkillCard(models.Model):
    title = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.title


# Work experience cards for the resume section
class WorkExperience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, help_text="Company or Role Subtitle")
    description = models.TextField()

    def __str__(self):
        return self.title

# Projects: Each project card with an image, description and a URL for further details.
class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(help_text="Short description of the project")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

# Social links (for footer): LinkedIn, GitHub, Email, etc.
class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=100, help_text="Icon name or CSS class", blank=True)

    def __str__(self):
        return self.platform

# Footer: Holds logo, text and related social links.
class Footer(models.Model):
    logo = models.ImageField(upload_to='footer/', blank=True, null=True)
    text = models.TextField(default="I build engaging, fast and high quality websites your users will love. I love JavaScript. And I am from Guwahati, Assam.")
    social_links = models.ManyToManyField(SocialLink, blank=True)

    def __str__(self):
        return "Footer Information"
