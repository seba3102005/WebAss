from rest_framework import serializers
from django.contrib.auth import get_user_model
from user.models import Education,Languages,project,Certification,WorkExperience,Skills

user = get_user_model()

class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    # gender = serializers.CharField(max_length=10)
    # phoneNo = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length =128,write_only=True)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['username','email','phoneNo','gender','password']
        extra_kwargs = {'password':{'write_only':True}}

    ## override the function create in order to make the password hashed
    def create(self,validated_data):
        user_data = user.objects.create_user(**validated_data)
        return user_data
    
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['institution','graduation_year']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ['name','image']


class CertifiactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['name','organization','year']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['name','descriprion']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['name']


class AccountSerializer(serializers.ModelSerializer):

    my_education = EducationSerializer(many = True)
    my_languages = LanguageSerializer(many=True)
    my_projects = ProjectSerializer(many=True)
    my_certifications = CertifiactionSerializer(many=True)
    my_experience = ExperienceSerializer(many=True)
    my_skills = SkillSerializer(many=True)
    
    class Meta:
        model = user
        fields = ['about','title','description','hourly_rate','hours_week','video','my_education' ,'my_languages','my_projects','my_certifications','my_experience', 'my_skills']
     