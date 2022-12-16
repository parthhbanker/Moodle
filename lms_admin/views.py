from datetime import datetime
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

    return render(request, "category.html", {"data":data})

def addCategory(request):
    if request.method == 'POST':
        cat_name = request.POST['category_name']
        desc = request.POST['category_desc']

        obj = CategoryModel()
        obj.cat_name = cat_name
        obj.cat_desc = desc

        obj.save()
    
    return HttpResponseRedirect(reverse("category"))

def deleteCategory(request, id):
    data = CategoryModel.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse("category"))
    
    

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

        obj = CourseModel()
        obj.course_name = course_name
        obj.course_category = course_category
        obj.course_difficulty = course_difficulty
        obj.total_lesson = total_lesson
        obj.coucourse_desc = ""

        obj.save()

    return HttpResponseRedirect(reverse("course"))

def deleteCourse(request, id):
    data = CourseModel.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse("course"))

### 
# instructor pages 
###

def instructorList(request):
    data = InstructorModel.objects.all()
    return render(request, "instructor-list.html", {"data" : data})

def addInstructor(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']

        obj = InstructorModel()
        obj.ins_fname = fname
        obj.ins_lname = lname
        obj.ins_email = email
        obj.ins_phone = phone
        obj.ins_desc = description

        obj.save()
    
    return HttpResponseRedirect(reverse("instructor-list"))


def instructorDetail(request):
    return render(request, "instructor-details.html")

def deleteInstructor(request, id):
    data = InstructorModel.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse("instructor-list"))

###
# admin pages
###
def adminProfileSetting(request):
    return render(request, "admin-profile-setting.html")

def adminProfile(request):
    data = AdminModel.objects.all()
    return render(request, "admin-profile.html", {"data":data})
    # return render(request, "admin-profile.html", {"data":data})

def updateAdminProfile(request):
    obj = AdminModel.objects.get(id=1)
    obj.name = request.POST['fn']
    obj.display_name = request.POST['dn']
    obj.email = request.POST['email']
    obj.phone = request.POST['phone']
    obj.dob = request.POST['dob']

    obj.save()

    return HttpResponseRedirect(reverse('admin-profile'))

###
# enroll pages
###

def enrollHistory(request):
    data = EnrollStudentModel.objects.all()
    return render(request, "enroll-history.html", {"data" : data})

def enrollStudent(request):
    course = CourseModel.objects.all()
    student = AddStudentModel.objects.all()
    return render(request, "enroll-student.html", {"course" : course, "student" : student})

def enroll(request):
    if request.method == 'POST':
        student = request.POST['student']
        course = request.POST['course']
        email = request.POST['email']
        phone = request.POST['phone']

        obj = EnrollStudentModel()
        obj.student_name = student
        obj.student_email = email
        obj.course_name = course
        obj.student_phone = phone

        obj.save()

    return render(request, "enroll-student.html")

###
# settting pages 
###
def setting(request):
    data = WebSettingModel.objects.all() 
    return render(request, "settings.html", {"data":data})

def updateSetting(request):
    data = WebSettingModel.objects.get(id=1)
    data.store_name = request.POST['site-name']
    data.store_email = request.POST['site-email']
    data.site_copyright = request.POST['site-copyright']
    data.main_website = request.POST['site-url']
    data.website_desc = request.POST['fv-message']

    data.save()

    return HttpResponseRedirect(reverse('setting'))

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
    data = AddStudentModel.objects.all()
    return render(request, "students.html", {"data":data})

def addStudent(request):
    if request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        phone = request.POST['phone']
        dob_ = request.POST['dob']

        dob = datetime.strptime(dob_, "%m/%d/%Y").strftime('%Y-%m-%d')

        obj = AddStudentModel()
        obj.stu_fname = fname
        obj.stu_lname = lname
        obj.stu_email = email
        obj.stu_phone = phone
        obj.stu_dob = dob

        obj.save()

        return HttpResponseRedirect(reverse('student'))

def deleteStudent(request, id):
    data = AddStudentModel.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse("student"))
