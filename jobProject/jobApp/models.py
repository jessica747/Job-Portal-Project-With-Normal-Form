from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user_model(AbstractUser):
    display_name=models.CharField(max_length=100,null=True)
    USERTYPE=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker'),
    ]
    user_type=models.CharField(max_length=100,null=True)
    profile_picture=models.ImageField(upload_to='media/profilephoto',null=True)

    

class recruiter_info_model(models.Model):
    recuser=models.OneToOneField(Custom_user_model,on_delete=models.CASCADE,related_name= 'recruiterinfo')
    company_name=models.CharField(max_length=100,null=True)
    company_address=models.CharField(max_length=100,null=True)
    company_depreciation=models.TextField(null=True)


    
class seeker_info_model(models.Model):
    seekuser=models.OneToOneField(Custom_user_model,on_delete=models.CASCADE,related_name= 'seekerinfo')
    skill_set=models.CharField(max_length=100,null=True)
    resume_upload=models.FileField(upload_to='resume/seekerresume',null=True)


    
