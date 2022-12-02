from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from lms_admin.models import *


# Create your s here.
def default(request):
    return render(request, "index.html")
    

###
# course pages
###
def category(request):
    data = CategoryModel.objects.all()
    print(data[1].cat_name)
    return render(request, "category.html", {"data":data})

def addCategory(request):
    if request.method == 'POST':
        cat_name = request.POST['category_name']
        desc = request.POST['category_desc']

        obj = CategoryModel()
        obj.cat_name = cat_name
        obj.cat_desc = desc

        obj.save()
    
    return category(request)
    
    

def course(request):
    data = CourseModel.objects.all()
    data1 = CategoryModel.objects.all()
    return render(request, "courses.html" , {"data":data, "data1": data1})

def addCourse(request):
    if request.method == "POST":
        course_name = request.POST['course_name']
        course_category = request.POST['course_category']
        course_difficulty = request.POST['course_difficulty']
        total_lesson = request.POST['total_lesson']
        # course_desc = request.POST['course_desc']

        print("===================")
        print(total_lesson)
        print("===================")

        obj = CourseModel()
        obj.course_name = course_name
        obj.course_category = course_category
        obj.course_difficulty = course_difficulty
        obj.total_lesson = total_lesson
        obj.coucourse_desc = ""

        obj.save()

    return course(request)

### 
# instructor pages 
###

def instructorList(request):
    return render(request, "instructor-list.html")

def instructorDetail(request):
    return render(request, "instructor-details.html")

###
# admin pages
###
def adminProfileSetting(request):
    return render(request, "admin-profile-setting.html")

def adminProfile(request):
    data = AdminModel.objects.all() 
    print(data[0].name)
    return render(request, "admin-profile.html", {"data":data})
    # return render(request, "admin-profile.html", {"data":data})

###
# enroll pages
###

def enrollHistory(request):
    return render(request, "enroll-history.html")

def enrollStudent(request):
    return render(request, "enroll-student.html")

###
# settting pages 
###
def setting(request):
    data = WebSettingModel.objects.all() 
    return render(request, "settings.html", {"data":data})\

###
# Student pages 
###

def studentInvoiceDetail(request):
    return render(request, "student-invoice-details.html")

def studentInvoiceList(request):
    return render(request, "student-invoice-list.html")

def studentInvoicePrint(request):
    return render(request, "student-invoice-print.html")

def studentDetailsCourses(request):
    return render(request, "students-details-courses.html")

def studentDetails(request):
    return render(request, "students-details.html")

def student(request):
    return render(request, "students.html")