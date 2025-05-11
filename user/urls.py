from django.urls import path,include
from .views import LoginView,RegisterView,AccountView,AddSKill
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AddSKill,basename='add')

urlpatterns  = [
    path('login/',LoginView.as_view(),name='login form'),  # login
    path('register/',RegisterView.as_view(),name='register form'),  # register
    path('account/<int:pk>/',AccountView.as_view(),name = 'My Account'),  # update any thing in the profile page
    path('add/<str:keyword>/', include(router.urls)),
    
]