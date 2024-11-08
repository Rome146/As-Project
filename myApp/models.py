from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    contact_no=models.CharField(max_length=100,null=True)
    
    def __str__(self):   
        
        return f"{self.username}"
    
class seekerProfileModel(models.Model):
    Skills = [
        ('Django','Django'),
        ('Python','Python'),
        ('Html','Html'),
    ]
    
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='seekerProfile')
    Skill = models.CharField(choices=Skills, max_length=50,null=True)
   
    def __str__(self):
        return f"{self.user.username}"
    
    
class recruiterProfileModel(models.Model):
    
   
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='recruiterProfile')
    company_name = models.CharField(null=True, max_length=50)
   
    def __str__(self):
        return f"{self.user.username}"
    
    
    
class JobModel(models.Model):
    Category = [
        ('Part_Time','Part_Time'),
        ('Full_Time','Full_Time'),
    ]
    Skills = [
        ('Django','Django'),
        ('Python','Python'),
        ('Html','Html'),
    ]
    user = models.ForeignKey(customUser, on_delete=models.CASCADE,null=True)
    category = models.CharField(choices=Category, max_length=50,null=True)
    Skill = models.CharField(choices=Skills, max_length=50,null=True)
    Title = models.CharField(null=True, max_length=50)
    vecancy = models.IntegerField(null=True, max_length=50)
    Description = models.TextField(null=True, max_length=500)
    Image = models.ImageField(upload_to="Media/Job_pic",null=True)
    
    
class ApplyJobModel(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.CASCADE,null=True)
    Job = models.ForeignKey(JobModel, on_delete=models.CASCADE,null=True)
    cover = models.TextField(null=True)
    resume = models.FileField(upload_to="Media/Resume", max_length=100,null=True)
    Apply_pic = models.ImageField(upload_to="Media/Resume",null=True)
    Skill  = models.CharField(max_length=50,null=True)