from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(null=True,max_length=200)
  content = models.TextField()
  creation_date = models.DateTimeField()
  published_date = models.DateTimeField(null=True)
  
  def __str__(self):
    return self.title
  
