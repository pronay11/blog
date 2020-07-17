from django.db import models

class Author(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
       return self.name

class Category(models.Model):
    name= models.CharField(max_length=250)

    def __str__(self):
       return self.name       

class Post(models.Model):
    image=models.ImageField(blank=True,null=True,upload_to='blog_app')
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    view_count=models.IntegerField(default=True)
    tittle=models.CharField(max_length=80)
    description=models.TextField()
    created_dt=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.tittle