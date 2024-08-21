from django.db import models

# Create your models here.
class Holder(models.Model):
    # id=models.AutoField()
    gmail = models.EmailField(max_length=50)
    paswrd= models.TextField(max_length=20)
    st1=models.CharField(null=True,blank=True,max_length=30)
    st2=models.CharField(null=True,blank=True,max_length=30)
    st3=models.CharField(null=True,blank=True,max_length=30)
    st4=models.CharField(null=True,blank=True,max_length=30)
    st5=models.CharField(null=True,blank=True,max_length=30)
    
    # def __str__(self):
    #     self.gmail
