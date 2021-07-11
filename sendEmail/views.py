from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import studentSerializer
from rest_framework.response import Response
from rest_framework import status ,viewsets
from django.conf import settings
from django.contrib import auth
from .models import students
from .serializers import studentSerializer
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from smtp.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT,EMAIL_HOST
# Create your views here.


def sendmail(subject, tolist, content):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    mail_content = content

    # The mail addresses and password
    from_address = EMAIL_HOST_USER
    from_pass = EMAIL_HOST_PASSWORD
    to_address = tolist.split(',')  # from input parameter

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = "," . join (to_address) 
    print("," . join (to_address) )
    message['Subject'] = subject  # from input parameter

    # The body and the attachments for the mail (if any - as of now, it is a plain mail)
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    # use gmail with port
    session = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    # enable security
    session.starttls()
    # login with mail_id and password
    session.login(from_address, from_pass)

    text = message.as_string()
    
    session.sendmail(from_address, to_address, text)
    session.quit()
    print('Mail Sent successfully')
    return

class SendEmailView(GenericAPIView):

    serializer_class = studentSerializer

    def post(self, request):
        serializer = studentSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            print("request data is " + serializer.data.get('email'))
            # I harcoded the data here please change accordingly
            sendmail('LMS Notifcation', serializer.data.get('email'), 'Notification For LMS Dashboard! added a quiz / assignments,etc')
            return Response(serializer.data, status=status.HTTP_200_OK)

class SendEmailViewCourse(GenericAPIView):

    serializer_class = studentSerializer

    def post(self, request):
        serializer = studentSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            print("request data is " + serializer.data.get('email'))
            # I harcoded the data here please change accordingly
            sendmail('LMS Notifcation', serializer.data.get('email'), 'Notification For LMS Dashboard! added a New Course')
            return Response(serializer.data, status=status.HTTP_200_OK)

class SendEmailAssignment(GenericAPIView):

    serializer_class = studentSerializer

    def post(self, request):
        serializer = studentSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            print("request data is " + serializer.data.get('email'))
            # I harcoded the data here please change accordingly
            sendmail('LMS Notifcation', serializer.data.get('email'), 'Notification For LMS Dashboard! added a new assignment')
            return Response(serializer.data, status=status.HTTP_200_OK)



class addstudentsinView(GenericAPIView):
    serializer_class = studentSerializer
    def post(self, request):
        serializer = studentSerializer(data=request.data, context={'request': request})
        #I harcoded the data here please change accordingly
        print("request data is")
        if serializer.is_valid():
            #sendmail('test Subjectmain code', 'asasas123@grr.la', 'Test Contentx')
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

class getAllstudentsinView(viewsets.ModelViewSet):
    queryset = students.objects.all().order_by('id')
    serializer_class = studentSerializer