from django.db import models

# Create your models here.
# (ORM) Object Relational Mapping

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)

class Blog(models.Model):
    BlogId = models.AutoField(primary_key=True)
    BlogName = models.CharField(max_length=500)
    BlogContent = models.CharField(max_length=2000)
    BlogTag = models.CharField(max_length=500)
    PostDate = models.DateField()
    BlogUserId = models.IntegerField(null=False)



    
