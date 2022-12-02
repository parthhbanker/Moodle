from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    cat_id = models.AutoField
    cat_name = models.CharField(max_length=255)
    cat_desc = models.TextField()


# class AddInstructorModel(models.Model):
#     ins_id = models.AutoField
#     ins_fname = models.CharField(max_length=255)
#     ins_lname = models.CharField(max_length=255)
#     ins_email = models.EmailField(max_length=255)
#     ins_phone = models.CharField(max_length=12)
#     ins_desc = models.TextField()
    
# class AddStudentModel(models.Model):
#     stu_id = models.AutoField
#     stu_fname = models.CharField(max_length=255)
#     stu_lname = models.CharField(max_length=255)
#     stu_email = models.EmailField(max_length=255)
#     stu_phone = models.CharField(max_length=12)

# class EnrollStudentModel(models.Model):
#     enr_id = models.AutoField
#     stu_id = models.IntegerField()
#     cid = models.IntegerField()
