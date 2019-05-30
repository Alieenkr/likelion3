from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    #image_url = models.TextField(blank=True)
    blog_image = models.ImageField(upload_to='blog_image/', blank=True)
    pub_date = models.DateTimeField("data published")
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("data published")

    def __str__(self):
        return self.body