from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LoginSerializer,RegisterSerializer,AccountSerializer,SkillSerializer,EducationSerializer,LanguageSerializer,ProjectSerializer,CertifiactionSerializer,ExperienceSerializer
from django.contrib.auth import authenticate,get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import CreateAPIView,UpdateAPIView,ListAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from user.models import Education,Languages,project,Certification,WorkExperience,Skills
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError

user = get_user_model()
# Create your views here.

class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email').strip()
        password = serializer.validated_data.get('password').strip()
        

        try:
            user_data = authenticate(username=email, password=password)
        except Exception as e:
            
            return Response({'error': 'Authentication error', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if user_data is None:
           
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            refresh = RefreshToken.for_user(user_data)
            return Response({"user":{"id":user_data.id,"username":user_data.username,"email":user_data.email,"phoneNo":user_data.phoneNo,"gender":user_data.gender},"refresh":str(refresh),"access":str(refresh.access_token)},status=status.HTTP_200_OK)


class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    queryset = user.objects.all()


class AccountView(RetrieveAPIView):
    queryset = user.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer
    lookup_field = 'pk'

class AddSKill(ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    
    
# override the function that gets the serializer class
    def get_serializer_class(self):
        keyword = self.kwargs.get('keyword')
        
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
        elif keyword == 'skill':
            return SkillSerializer
        else:
            raise ValidationError({'error': 'The keyword is not valid'})


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
        elif keyword == 'skill':
            return Skills.objects.all()
        else:
            raise ValidationError({'error': 'The keyword is not valid'})
         
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    
    def create(self, request, *args, **kwargs):
        keyword = self.kwargs.get('keyword')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"created":f'you {keyword} is added successfully'}, status=status.HTTP_201_CREATED)