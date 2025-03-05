# In your admin.py (typically in your project or app directory)
from django.contrib import admin

admin.site.site_header = "My Portfolio Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to the Portfolio Admin"


from django.contrib import admin
from .models import Skill, SkillCard, WorkExperience, Project, SocialLink, Footer

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SkillCard)
class SkillCardAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('skills',)  # If you want to manage the many-to-many relationship

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'start_date', 'end_date')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url')

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('text',)