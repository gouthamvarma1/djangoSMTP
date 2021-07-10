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
# Create your views here.


def sendmail(subject, tolist, content):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    mail_content = content

    # The mail addresses and password
    from_address = 'bitsassignment111@gmail.com'
    from_pass = 'BitsPassword$1'
    to_address = tolist  # from input parameter

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = ", ".join(to_address)
    message['Subject'] = subject  # from input parameter

    # The body and the attachments for the mail (if any - as of now, it is a plain mail)
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    # use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)
    # enable security
    session.starttls()
    # login with mail_id and password
    session.login(from_address, from_pass)

    text = message.as_string()
    session.sendmail(from_address, to_address, text)
    session.quit()
    print('Mail Sent to '+ to_address)
    return

class SendEmailView(GenericAPIView):

    serializer_class = studentSerializer

    def post(self, request):
        serializer = studentSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            print("request data is" + serializer.data.get('email'))
            # I harcoded the data here please change accordingly
            sendmail('test Subjectmain code', serializer.data.get('email'), 'Test Contentx')
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