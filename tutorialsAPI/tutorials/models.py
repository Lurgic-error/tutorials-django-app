from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(blank=False, default='')
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'tutorial'
        verbose_name_plural = 'tutorials'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('tutorial_details', kwargs = {'pk' : self.id})