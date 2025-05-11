# from django.db import models
# from django.core.validators import MinValueValidator,MaxValueValidator
# # Create your models here.



# class Client(models.Model):
#     name = models.CharField(max_length=100)







# class JobOffers(models.Model):

#     difficulty_choices = [('beginner','beginner'),('intermediate','intermediate'),('expert','expert')]

#     client_id = models.ForeignKey(Client,on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     location = models.CharField(max_length=100)
#     project_length = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
#     hours = models.IntegerField(validators=[MaxValueValidator(30),MinValueValidator(1)])
#     difficulty = models.CharField(choices=difficulty_choices,max_length=15)
#     job_link = models.URLField()
#     no_proposals = models.IntegerField(default=0)
#     is_available = models.BooleanField(default=False)


    
