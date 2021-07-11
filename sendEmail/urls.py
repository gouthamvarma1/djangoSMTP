
from django.urls import include,path
from rest_framework import routers

from .views import SendEmailView,addstudentsinView,SendEmailViewModule,SendEmailAssignment
from . import views


router = routers.DefaultRouter()
router.register(r'/viewAllstudents', views.getAllstudentsinView)

urlpatterns = [
    path('/sendEmail',SendEmailView.as_view()), # used for sending Email for New Quiz
    path('/sendEmailModule',SendEmailViewModule.as_view()),# used for sending Email for New Module
    path('/sendEmailAssignment',SendEmailAssignment.as_view()),# used for sending Email for New Assignment
    path('/addstudent',addstudentsinView.as_view()),
    path('', include(router.urls))
    #path('_viewAllstudents',getAllstudentsinView.as_view())
]