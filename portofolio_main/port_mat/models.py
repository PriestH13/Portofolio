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
