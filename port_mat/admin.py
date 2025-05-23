from django.contrib import admin
from .models import Projects, ProjectImage, Service, About, ContactInfo, Intro


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'description'] 

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'technologies', 'github_link', 'demo_link')
    search_fields = ['title', 'technologies']
    inlines = [ProjectImageInline]


class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'description')
    search_fields = ['description']

admin.site.register(Projects, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(Service)
admin.site.register(About)
admin.site.register(ContactInfo)
admin.site.register(Intro)
