
from django.urls import include,path
from rest_framework import routers

from .views import SendEmailView,addstudentsinView
from . import views


router = routers.DefaultRouter()
router.register(r'/viewAllstudents', views.getAllstudentsinView)

urlpatterns = [
    path('_sendEmail',SendEmailView.as_view()),
    path('_addstudent',addstudentsinView.as_view()),
    path('', include(router.urls))
    #path('_viewAllstudents',getAllstudentsinView.as_view())
]