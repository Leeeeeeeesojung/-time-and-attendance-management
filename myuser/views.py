from asyncio.windows_events import NULL
from datetime import date, datetime
from email.policy import HTTP
from operator import truediv
from telnetlib import DO
from urllib import response
from django.forms import DateTimeField
from django.shortcuts import render, redirect
from requests import Response
from scipy.misc import central_diff_weights
from .models import Myuser, Document, Center, Test
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
from django.views.decorators.csrf import csrf_exempt
from insightface_deploy import test_image
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views import View
from django.http import JsonResponse
import json

def userinfoToJson(myuser):
    if myuser == None:
        return None
    jsondata = {}
    jsondata["username"] = myuser.username
    jsondata["email"] = myuser.email
    jsondata["position"] = myuser.position
    jsondata["department"] = myuser.department
    jsondata["datetime"] = datetime.now()
    jsondata["response"] = "1"

    return jsondata
# Create your views here.
model, model1 ,f = test_image.init()
def home(request):
    user_id = request.session.get('user')
    if user_id :
        myuser_info = Myuser.objects.get(pk=user_id)  #pk : primary key
        return HttpResponse(myuser_info.username)

    return HttpResponse('로그인 완료.')


@csrf_exempt
#출근
def login(request): #출근
    response_data = {}
    global username

    if request.method == "GET" :
    
        return render(request, 'login.html')

    elif request.method == "POST":
            
            # fileTitle = request.POST.get('text',False)
            uploadFile = request.FILES['image']   
            document = Document(
            uploadedFile=uploadFile,
            )
            document.save()
         
            print(uploadFile)
            flag,login_username = test_image.check(model, model1, f, uploadFile)
            print(flag,login_username)
            flag = Myuser.objects.filter(username=login_username).exists()
            print(Myuser.objects.filter(username=login_username))
            if flag:
                myuser = Myuser.objects.get(username=login_username)
                username = myuser.username,
                email = myuser.email,
                position = myuser.position,
                department = myuser.department,
                
            else:
                return HttpResponse("fail")

            print(myuser, username, email, position, department)

            test = Test(
            username = username,
            position = position,
            department = department,
            dateTimeOfAM = datetime.now()
            )
            test.save()

            e_mail = myuser.email
            mail_subject = '이메일 보냅니다!'
            message = render_to_string('smtp_email.html', {
            'name': ''
                })
            to_email = e_mail
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            jsondata = userinfoToJson(myuser)
            return JsonResponse(jsondata) 

@csrf_exempt
#퇴근
def logout(request):  #퇴근/ 이미지 파일을 가져와서 이미지 이름 ~~, 이름으로 기존 db에 있는 해당하는 유저의 정보를 가져오기
    response_data = {}

    if request.method == "POST":
   
        uploadFile = request.FILES['image']    
        document = Document(
        uploadedFile=uploadFile,
        )
        document.save()

        #가장 최근에 작성된 db, 유저이름
        flag, logout_username = test_image.check(model, model1, f, uploadFile)
        print(flag, logout_username)
        flag = Myuser.objects.filter(username=logout_username).exists()
        print(Myuser.objects.filter(username=logout_username))
        if flag:
            myuser = Myuser.objects.get(username=logout_username)
            username=myuser.username,
            email=myuser.email,
            position = myuser.position,
            department = myuser.department,

        else:
            return HttpResponse("fail")
            
        print(myuser, username, email, position, department)
        
        test = Test.objects.filter(username=username).last()
        test.dateTimeOfPM = datetime.now()
        test.save()

        jsondata = userinfoToJson(myuser)
        return JsonResponse(jsondata)

@csrf_exempt
#점심시간
def lunch(request):
    response_data = {}

    if request.method == "POST":

        fileTitle = request.POST['text']
        uploadFile = request.FILES['image']
        document = Document(
            title = fileTitle,
            uploadedFile=uploadFile,
        )
        document.save()

        flag, lunch_username = test_image.check(model, model1, f, fileTitle)
        print(flag, lunch_username)
        flag = Myuser.objects.filter(username=lunch_username).exists()
        print(flag, Myuser.objects.filter(username=lunch_username))
        if flag:
            myuser = Myuser.objects.get(username=lunch_username)
            username=myuser.username,
            email=myuser.email,
            position = myuser.position,
            department = myuser.department,
        else:
            return HttpResponse("fail")

        print(myuser, username, email, position, department)
        
        center = Center(
        username = username,
        position = position,
        department = department,
        middleTime = datetime.now()
        )
        center.save()

        center = datetime.now()
        center = Center.objects.filter(username=username, middleTime__contains = "2022-05%")
        return HttpResponse("succcess")
        
@csrf_exempt
#회원가입
def register(request):  #나중에 html의 url을 연결하면 변수가 이곳을통해 request로 들어온다.
    #html의 name값으로 들어오게된다.
    response_data = {}
    if request.method == "GET" : #일반적으로 url입력을 통해 들어왔을때
        return render(request, 'register.html')
    elif request.method == "POST":
         #submit버튼을 눌렀을때
        username = request.POS.get('username')     #POST로 딕셔너리형태로 넘어오기때문에 이렇게.... 되는구나
        email = request.POST.get('email')           #만약 email 이라는 key에 해당하는 value가 없다면 None을 넘기게됌.
        password = request.POST.get('password')
        position = request.POST.get('position')
        department = request.POST.get('department')
        uploadFile = request.FILES['image']   
        document = Document(
        uploadedFile=uploadFile,
        )
        document.save()

        flag = Myuser.objects.filter(username=username).exists()
        print(flag, Myuser.objects.filter(username=username))
        if flag:
                myuser = Myuser.objects.get(username=username)
                username=myuser.username,
                email=myuser.email,
                password=myuser.password,
                position = myuser.position,
                department = myuser.department,
                
                jsondata = {}
                jsondata["username"] = username
                # jsondata["datetime"] = datetime.now()
                jsondata["response"] = "1"
                return JsonResponse(jsondata)
        else:
            myuser = Myuser(
            username=username,
            email=email,
            password= make_password(password),
            position = position,
            department = department,
            )
           
            myuser.save()

            jsondata = {}
            jsondata["username"] = username
            # jsondata["datetime"] = datetime.now()
            jsondata["response"] = "1"
            return JsonResponse(jsondata)

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        fileTitle = request.POST['text']
        uploadFile = request.FILES['image']
        document = Document(
            title=fileTitle,
            uploadedFile=uploadFile
        )
        document.save()

    return HttpResponse(fileTitle) 
@csrf_exempt
def face(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'face.html')

    elif request.method == "POST":
        fileTitle = request.POST['text']
        uploadFile = request.FILES['image']    
        document = Document(
            title=fileTitle,
            uploadedFile=uploadFile
        )
        document.save()                                       
        
        
        re = test_image.check(model, model1, f, fileTitle)
         #이미지를 받아서 여기에다가 변수로 넘겨줌
        
        return HttpResponse(re)