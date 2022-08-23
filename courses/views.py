from django.shortcuts import render
from .models import Courses
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    courses = Courses.objects.all()

    return render(request,'home.html',{'courses':courses,'message':"merhaba Clarusway"})

def course_detail(request,id):
    course=Courses.objects.get(id=id)

    return render(request,'detail.html',{'course':course})