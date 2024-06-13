'''
from django.urls import path,include
from . import views

urlpatterns = [

#path("",views.InsertPageView,name="insertpage"),
#path("insert/",views.InsertData,name="insert"),
#path("showpage/",views.ShowPage,name="showpage"),
#path("editpage/<int:pk>",views.EditPage,name="editpage"),
#path("update/<int:pk>",views.UpdateData,name="update"),
#path("delete/<int:pk>",views.DeleteData,name="delete"),
#path("",views.RegisterPage,name="registerpage"),
#path("register/",views.UserRegister,name="register"),
#path("loginpage/",views.LoginPage,name="loginpage"),
#path("loginUser/",views.LoginUser,name="login"),
#path("",views.IndexPage,name="index"),
#path("upload/",views.UploadImage,name='imageupload'),
#path("showing/",views.ImageFetch,name="show"),
]

'''
#from django.contrib import admin  
from django.urls import path, include  
from .views import StudentView  
from .import views
from django.urls import path  
  
urlpatterns = [
    path('basic/', StudentView.as_view()), 
    path('basic/<int:id>/', StudentView.as_view()),
    path('basic/<int:id>/update/', StudentView.as_view()) 
]
