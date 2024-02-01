from django.db import models

# Create your models here.

class dbportfolio(models.Model):
    code = models.SlugField(verbose_name="Clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    description = models.CharField(verbose_name="Description",max_length= 300)
    url = models.URLField(verbose_name="Link", max_length=200, null=True, blank=True)
    image = models.ImageField(verbose_name="Image", upload_to="folio/static/img")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "PortFolios"
        ordering = ['name']
        
    def __str__(self):
        return self.name 
   