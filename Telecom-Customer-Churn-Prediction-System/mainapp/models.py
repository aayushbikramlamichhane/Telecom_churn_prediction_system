from django.db import models

# Create your models here.

class Contact(models.Model):
    
    ename=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    emailadd=models.EmailField()
    num=models.IntegerField()
    message=models.TextField()
    # def __str__(self):
    #     return self.ename
    

class Customer(models.Model):
    
    customer_name=models.CharField(max_length=200)
    customer_address=models.CharField(max_length=200)
    customer_email=models.EmailField()
    contact_number=models.IntegerField()
    
class RegUsers(models.Model):
    cName=models.CharField(max_length=200)
    cBranch=models.CharField(max_length=200)
    cNumber=models.IntegerField()
    cEmail=models.EmailField()
    cUsername=models.CharField(max_length=200)
    