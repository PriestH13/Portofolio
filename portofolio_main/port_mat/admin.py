from django.contrib import admin
from .models import Projects, ProjectImage

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'technologies', 'github_link', 'demo_link')
    search_fields = ['title', 'technologies']  

class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'description')  
    search_fields = ['description'] 

# Registrare i modelli con la personalizzazione
admin.site.register(Projects, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
