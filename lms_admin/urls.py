from django.urls import path
from . import views

urlpatterns = [
	path("", views.default, name="home"),
	path('index/', views.default, name="index"),
	
	# adminProfile
	path('admin-profile-settings/', views.adminProfileSetting, name="admin-settings"),
	path('admin-profile/', views.adminProfile, name="admin-profile"),
	path('update-admin-profile/', views.updateAdminProfile, name="update-admin-profile"),

	# course
	path('category/', views.category, name="category"),
	path('addCategory', views.addCategory, name="add-category"),
	path('addCourse', views.addCourse, name="add-course"),
	path('course/', views.course, name="course"),
	# del
	path('delCategory/<int:id>', views.deleteCategory, name="del-category"),
	path('delCourse/<int:id>', views.deleteCourse, name="del-course"),

	# enroll
	path('enroll-history/', views.enrollHistory, name="enroll-history"),
	path('enroll-students/', views.enrollStudent, name="enroll-students"),
	path('enroll', views.enroll, name="enroll"),

	# instructor
	path('instructor-list/', views.instructorList, name="instructor-list"),
	path('addinstructor', views.addInstructor, name="add-instructor"),
	path('instructor-details/', views.instructorDetail, name="instructor-details"),
	# del
	path('delInstructor/<int:id>', views.deleteInstructor, name="del-instructor"),

	# setting
	path('setting/', views.setting, name="setting"),
	path('update-setting', views.updateSetting, name="update-setting"),

	# student
	path('student-invoice-details/', views.studentInvoiceDetail, name="student-invoice-details"),
	path('student-invoice-list/', views.studentInvoiceList, name="student-invoice-list"),
	path('student-invoice-print/', views.studentInvoicePrint, name="student-invoice-print"),
	path('student-details-courses/', views.studentDetailsCourses, name="student-details-courses"),
	path('student-details/', views.studentDetails, name="student-details"),
	path('students', views.student, name="student"),
	# add
	path('addStudent', views.addStudent, name="add-student"),
	# del
	path('delStudent/<int:id>', views.deleteStudent, name="del-student"),

]
