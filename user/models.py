from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.


class NewUserManager(BaseUserManager):

    def create_user(self,email,password,gender,phoneNo,username,**kwargs):
        if not email:
            raise ValueError('You must provide an email address')
        norm_email = self.normalize_email(email)
     

        user = self.model(email=norm_email,gender=gender,phoneNo=phoneNo,username=username,is_active=True,**kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,username,gender,phoneNo,**kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email=email,username=username,password=password,phoneNo=phoneNo,gender=gender ,is_active=True,**kwargs)


class NewUser(AbstractBaseUser,PermissionsMixin):
    choices = [('male','male'),('female','female')]

    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    gender = models.CharField(max_length=10,choices=choices)
    phoneNo = models.CharField(max_length=11)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)   # by default is false when i want to implement that user can activate it account
    title = models.CharField(max_length=100,default='Title')
    description = models.TextField(max_length=500,default='Description')
    hourly_rate = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)],default='1')
    hours_week = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(30)],default=1)
    video = models.FileField(upload_to='videos/',null=True)
    

    objects = NewUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('gender','phoneNo','username')

    def __str__(self):
        return self.username


class Education(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='my_education')
    institution = models.CharField(max_length=100)
    graduation_year = models.DateField()
    def __str__(self):
        return self.institution


class Languages(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name = 'my_languages')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class project(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='my_projects')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imgs/')
    def __str__(self):
        return self.name


class Certification(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='my_certifications')
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    year = models.DateField()
    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='my_experience')
    description = models.TextField(max_length=100)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skills(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='my_skills')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    




