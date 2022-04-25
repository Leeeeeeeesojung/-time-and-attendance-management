from time import time
from django.db import models
from django.forms import ImageField

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="result/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

class Myuser(models.Model): #회원정보
    username= models.CharField(max_length = 64, verbose_name='사용자명')  
    # verbose_name(장황한 이름?) 을 설정해주면 관리자페이지에서 username대신에 '사용자명'으로 뜬다.
    email = models.EmailField(max_length=128, verbose_name='이메일')
    password = models.CharField(max_length = 64, verbose_name = '비밀번호')
    registered_time = models.DateTimeField(auto_now_add=True, verbose_name = '등록시간')
    #DateTimeField옵션 auto_now_add 현재시간 자동삽입.
    imagename = models.CharField(max_length = 64, null =  True, verbose_name = '이미지 이름')
    #직책 및 부서 추가
    position = models.CharField(max_length=64, verbose_name='직책', null=True)
    department = models.CharField(max_length=64, verbose_name='부서', null=True)

    def __str__(self):  #admin페이지의 
        return self.username
    class Meta :   #메타 클래스 _ 테이블을 이름 직접 설정할때. https://docs.djangoproject.com/en/3.0/ref/models/options/
        db_table = 'community_myuser'
        verbose_name = "사용자들(Meta)클래스"
        verbose_name_plural = "사용자들(Meta)클래스"

class Time(models.Model): #회원정보: 출퇴근 시간 기록 보관, 시간, 사람이름, 부서, 직책
    dateTimeOfAM = models.DateTimeField(auto_now=True, verbose_name='출근시간')
    dateTimeOfPM = models.DateTimeField(default="null", verbose_name='퇴근시간')
    username= models.CharField(max_length = 64, verbose_name='사용자명')
    position = models.CharField(max_length=64, verbose_name='직책')
    department = models.CharField(max_length=64, verbose_name='부서')
    

