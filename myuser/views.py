from datetime import date, datetime
from urllib import response
from django.forms import DateTimeField
from django.shortcuts import render, redirect
from .models import Myuser, Document, Time
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
from django.views.decorators.csrf import csrf_exempt
from insightface_deploy import test_image
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.
model, model1 ,f = test_image.init()
def home(request):
    user_id = request.session.get('user')
    if user_id :
        myuser_info = Myuser.objects.get(pk=user_id)  #pk : primary key
        return HttpResponse(myuser_info.username)

    return HttpResponse('로그인 완료.')



def login(request): #출근
    response_data = {}
    
    if request.method == "GET" :
    
        return render(request, 'login.html')

    elif request.method == "POST":



            fileTitle = request.POST['text']   
            uploadFile = request.FILES['image']   
            document = Document(
            title=fileTitle,
            uploadedFile=uploadFile,
            )
            document.save()
            

            re, logout_username = test_image.check(model, model1, f, fileTitle)
            myuser = Myuser.objects.get(username=logout_username)
            username=Myuser.username,
            email = Myuser.email,
            position = Myuser.position,
            department = Myuser.department,           

            dateTimeOfUpload = request.POST['text']
            time = Time(
            username = Myuser.username,
            position = Myuser.position,
            department = Myuser.department,
            dateTimeOfAM = datetime.now
            )
            time.save()

            e_mail = myuser.email
            mail_subject = '이메일 보냅니다!'
            message = render_to_string('smtp_email.html', {
            'name': ''
                })
            to_email = e_mail
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return render(request, 'login.html',response_data)


def logout(request):  #퇴근/ 이미지 파일을 가져와서 이미지 이름 ~~, 이름으로 기존 db에 있는 해당하는 유저의 정보를 가져오기
    response_data = {}

    if request.method == "POST":
        fileTitle = request.POST['text']    
        uploadFile = request.FILES['image']    
        document = Document(
        title=fileTitle,
        uploadedFile=uploadFile,
        )
        document.save()

        #가장 최근에 작성된 db, 유저이름 
        re, logout_username = test_image.check(model, model1, f, fileTitle)
        myuser = Myuser.objects.get(username=logout_username)
        username=Myuser.username,
        email=Myuser.email,
        position = Myuser.position,
        department = Myuser.department,
       
        time = Time.objects.filter(username=username).filter(dateTimeOfPM="null")     
        time.dateTime2 = datetime.now
        time.save()

    return redirect('/')


def register(request):  #나중에 html의 url을 연결하면 변수가 이곳읉롱해 request로 들어온다.
    #html의 name값으로 들어오게된다.
    response_data = {}

    if request.method == "GET" : #일반적으로 url입력을 통해 들어왔을때
        return render(request, 'register.html')
    elif request.method == "POST": #submit버튼을 눌렀을때
        username = request.POST.get('username', None)             #POST로 딕셔너리형태로 넘어오기때문에 이렇게.... 되는구나
        email = request.POST.get('email', None)                   #만약 email 이라는 key에 해당하는 value가 없다면 None을 넘기게됌.
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        imagename = request.POST.get('imagename', None)
        position = request.POST.get('position', None)
        department = request.POST.get('department',None)
        # if password != re_password :
        print(username, email, password, re_password, imagename, position, department)
        #     return HttpResponse("비밀번호가 다릅니다.")   # 페이지를 바꾸어 메시지 출력하는 메소드
        if not(username and password  and email and imagename and position and department):
            response_data['error'] = '모든 값을 입력해야 합니다.'

        else : 
            myuser = Myuser(
            username=username,
            # password = password
            email=email,
            password= make_password(password),
            imagename = imagename,
            position = position,
            department = department,
            )
            fileTitle = request.POST['text']    #1 원본 사진과 갱신되는 사진 파일명을 구분되게 바꿔줘야함. 근데 크게 신경 안써도 된다고 하심.
            uploadFile = request.FILES['image']    #2 갱신되는 사진은 지워져야되는데 어떻게 해야 할지,,,,,?
            document = Document(
            title=fileTitle,
            uploadedFile=uploadFile,
            )
            document.save()
            myuser.save()
        return render(request, 'register.html', response_data)

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