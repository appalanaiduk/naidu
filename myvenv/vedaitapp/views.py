'''
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def RegisterPage(request):
    return render(request,"app/register.html")




#view for user registration
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        #First we validate that user already exit

        user = User.objects.filter(Email=email)

        if user:
            message = "User already exist"
            return render(request,"app/login.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)

                message = "User register Successfully"
                return render(request,"app/login.html",{'msg':message})
            else:
                message = "Password and Confirm Password Doesnot Match"
                return render(request,"app/register.html",{'msg':message})

def LoginPage(request):
    return render(request,"app/login.html")

#Login User

def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        

        #checking the emailid with database
        user = User.objects.get(Email=email)

        if user:
            if user.Password == password:
                #we are getting user data in session
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                
                return render(request,"app/home.html")
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
'''
'''
def IndexPage(request):
    return render(request,"app/index.html")

def UploadImage(request):
    if request.method=="POST":
        imagename=request.POST['imgname']
        pics=request.FILES['image']
        
        newimg = ImageData.objects.create(Imagename=imagename,Image=pics)
        #return render(request,"app/show.html")
        return redirect('show')

def ImageFetch(request):
    all_img=ImageData.objects.all()
 
    return render(request,"app/show.html",{'key1':all_img})
'''
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Students  
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404  
# Create your views here.  
  
class StudentView(APIView):  
        
        def get(self, request, id):
            result = Students.objects.get(id=id)
            if id:
                serializers = StudentSerializer(result)
                return Response({'status': 'success', "students":serializers.data}, status=200)  
            result = Students.objects.all()
            serializers = StudentSerializer(result, many=True)
            return Response({'status': 'success', "students":serializers.data}, status=200)  
        
        def post(self, request):  
            serializer = StudentSerializer(data=request.data)  
            if serializer.is_valid():  
                serializer.save()  
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
            else:  
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    
        def patch(self, request, id):
            result = Students.objects.get(id=id)  
            serializer = StudentSerializer(result, data = request.data, partial=True)  
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})  
            else:
                return Response({"status": "error", "data": serializer.errors})  

    
        def get(self, request, *args, **kwargs):  
            result = Students.objects.all()  
            serializers = StudentSerializer(result, many=True)  
            return Response({'status': 'success', "students":serializers.data}, status=200)  
        
        
        def delete(self, request, id=None):
            result = get_object_or_404(Students, id=id)
            result.delete()
            return Response({"status": "success", "data": "Record Deleted"})