from django.contrib import admin
from .models import NewUser,Education,Languages,project,Certification,WorkExperience,Skills
# Register your models here.

admin.site.register(NewUser)
admin.site.register(Education)
admin.site.register(Languages)
admin.site.register(project)
admin.site.register(Certification)
admin.site.register(WorkExperience)
admin.site.register(Skills)