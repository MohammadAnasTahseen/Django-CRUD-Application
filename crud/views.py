from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from django.shortcuts import redirect

def home(request):
    stu=student.objects.all()
   # return HttpResponse("Hello, World!")
    return render(request,"stu/home.html",{'stu':stu})

def add_student(request):
    if request.method=="POST":
          print("ADDED SUCCESSFULLY")
          stu_roll=request.POST.get("stu_roll")
          stu_name=request.POST.get("stu_name")
          stu_email=request.POST.get("stu_email")
          stu_address=request.POST.get("stu_address")
          stu_phone=request.POST.get("stu_phone")


          s=student()
          s.roll=stu_roll
          s.name=stu_name
          s.email=stu_email
          s.address=stu_address
          s.phone=stu_phone


          s.save()
          return redirect("/crud/home")



    return render(request,"stu/add_student.html",{})

def delete_student(request,roll):
     s=student.objects.get(pk=roll)
     s.delete()

     return redirect("/crud/home")

def update_student(request, roll):
     
     stu=student.objects.get(pk=roll)
     
     return render(request,"stu/update_student.html",{'stu':stu})


def do_update_student(request,roll):
     
     stu_roll=request.POST.get("stu_roll")
     stu_name=request.POST.get("stu_name")
     stu_email=request.POST.get("stu_email")
     stu_address=request.POST.get("stu_address")
     stu_phone=request.POST.get("stu_phone")
     stu=student.objects.get(pk=roll)

     stu.roll=stu_roll
     stu.name=stu_name
     stu.email=stu_email
     stu.address=stu_address
     stu.phone=stu_phone
     stu.save()

     return redirect("/crud/home")

# Create your views here.
