from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

#Mailchimp Signup
'''class Signup(models.Model):
    email=models.EmailField(
        timestamp=models.DateTimeField(auto_now_add=True)
    )'''


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

    
    