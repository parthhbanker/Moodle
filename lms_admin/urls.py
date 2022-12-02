from django.urls import path
from . import views

urlpatterns = [
	path("", views.default, name="home"),
	path('index/', views.default, name="index"),
	
	# adminProfile
	path('admin-profile-settings/', views.adminProfileSetting, name="admin-settings"),
	path('admin-profile/', views.adminProfile, name="admin-profile"),

	# course
	path('category/', views.category, name="category"),
	path('addCategory', views.addCategory, name="add-category"),
	path('addCourse', views.addCourse, name="add-course"),
	path('course/', views.course, name="course"),

	# enroll
	path('enroll-history/', views.enrollHistory, name="enroll-history"),
	path('enroll-students/', views.enrollStudent, name="enroll-students"),

	# instructor
	path('instructor-list/', views.instructorList, name="instructor-list"),
	path('instructor-details/', views.instructorDetail, name="instructor-details"),

	# setting
	path('setting/', views.setting, name="setting"),

	# student
	path('student-invoice-details/', views.studentInvoiceDetail, name="student-invoice-details"),
	path('student-invoice-list/', views.studentInvoiceList, name="student-invoice-list"),
	path('student-invoice-print/', views.studentInvoicePrint, name="student-invoice-print"),
	path('student-details-courses/', views.studentDetailsCourses, name="student-details-courses"),
	path('student-details/', views.studentDetails, name="student-details"),
	path('students', views.student, name="student")

]
