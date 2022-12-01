from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your s here.
def default(request):
    return render(request, "index.html")
    

###
# course pages
###
def category(request):
    return render(request, "category.html")

def course(request):
    return render(request, "courses.html")

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
    return render(request, "admin-profile.html")

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
    return render(request, "settings.html")

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