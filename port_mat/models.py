from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Image for {self.project.title}'
    
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"    

class About(models.Model):
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Section"

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

class ContactInfo(models.Model):
    email = models.EmailField(max_length=254)
    linkedin_url = models.URLField(blank=True, null=True)
    linkedin_name = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(blank=True, null=True)
    github_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Contact Information"

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

class Intro(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    immagine = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.nome