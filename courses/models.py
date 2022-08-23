from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name=models.CharField(max_length=50)
    description= models.TextField()
    is_active=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
