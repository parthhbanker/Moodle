from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    cat_id = models.AutoField
    cat_name = models.CharField(max_length=255)
    cat_desc = models.TextField()

class CourseModel(models.Model):
    course_id = models.AutoField
    course_name = models.CharField(max_length=255)
    course_category = models.CharField(max_length=255)
    course_difficulty = models.CharField(max_length=255)
    total_lesson = models.IntegerField()
    course_desc = models.TextField()

class AdminModel(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)

class WebSettingModel(models.Model):
    id = models.AutoField
    store_name = models.CharField(max_length = 255)
    site_email = models.CharField(max_length=255)
    site_copyright = models.CharField(max_length = 255)
    allow_registration = models.IntegerField()
    main_website = models.CharField(max_length=255)
    website_desc = models.TextField()
    maintanance_mode = models.IntegerField()


class InstructorModel(models.Model):
    ins_id = models.AutoField
    ins_fname = models.CharField(max_length=255)
    ins_lname = models.CharField(max_length=255)
    ins_email = models.EmailField(max_length=255)
    ins_phone = models.CharField(max_length=20)
    ins_desc = models.TextField()
    
class AddStudentModel(models.Model):
    stu_id = models.AutoField
    stu_fname = models.CharField(max_length=255)
    stu_lname = models.CharField(max_length=255)
    stu_email = models.EmailField(max_length=255)
    stu_phone = models.CharField(max_length=12)
    stu_dob = models.DateField()

class EnrollStudentModel(models.Model):
    enr_id = models.AutoField
    student_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    student_phone = models.CharField(max_length=255)
    student_email = models.CharField(max_length=255)
