from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LoginSerializer,RegisterSerializer,AccountSerializer,SkillSerializer,EducationSerializer,LanguageSerializer,ProjectSerializer,CertifiactionSerializer,ExperienceSerializer
from django.contrib.auth import authenticate,get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import CreateAPIView,UpdateAPIView,ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from user.models import Education,Languages,project,Certification,WorkExperience,Skills
from rest_framework.viewsets import ModelViewSet

user = get_user_model()
# Create your views here.

class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email').strip()
        password = serializer.validated_data.get('password').strip()
        

        user = authenticate(email=email ,password=password)
        if not user:
            return Response({'error':'failed to authenticate the user'},status=status.HTTP_400_BAD_REQUEST)
        else:
            refresh = RefreshToken.for_user(user)
            return Response({"user":{"id":user.id,"username":user.username,"email":user.email,"phoneNo":user.phoneNo,"gender":user.gender},"refresh":str(refresh),"access":str(refresh.access_token)},status=status.HTTP_200_OK)


class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    queryset = user.objects.all()


class AccountView(ListAPIView):
    queryset = user.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer
    lookup_field = 'pk'

class AddSKill(ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    
    
# override the function that gets the serializer class
    def get_serializer_class(self):
        keyword = self.kwargs.get('keyword')
        print(keyword)
        if keyword == 'education':
            return EducationSerializer
        elif keyword == 'language':
            return LanguageSerializer
        elif keyword == 'project':
            return ProjectSerializer
        elif keyword == 'certification':
            return CertifiactionSerializer
        elif keyword == 'experience':
            return ExperienceSerializer
        return SkillSerializer 


# overrides the function that gets the quesry set of the model view set
    def get_queryset(self):
        keyword = self.kwargs.get('keyword')

        if keyword == 'education':
            return Education.objects.all()
        elif keyword == 'language':
            return Languages.objects.all()
        elif keyword == 'project':
            return project.objects.all()
        elif keyword == 'certification':
            return Certification.objects.all()
        elif keyword == 'experience':
            return WorkExperience.objects.all()
        return Skills.objects.all() 

    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)