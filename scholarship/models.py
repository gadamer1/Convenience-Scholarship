from django.db import models
from unidecode import unidecode
from django.utils.text import slugify
# Create your models here.


class Scholar_content(models.Model):
    #장학이름
    scholar_name=models.CharField(max_length=200,primary_key=True)
    #장학혜택
    scholar_reward=models.TextField(blank=True)
    #제출서류
    scholar_needs=models.TextField(blank=True)
    #접수방법
    scholar_howto=models.TextField(blank=True)
    #장학 문의 번호
    scholar_qna=models.TextField(blank=True)
    #선발인원
    scholar_recruitment_num=models.PositiveIntegerField()
    #모집기간
    scholar_application_start=models.DateTimeField(blank=True,null=True)
    scholar_application_end = models.DateTimeField(blank=True,null=True)
    #장학재단명
    scholar_foundation_name=models.CharField(max_length=200)
    #선발대상
    scholar_who_draft=models.TextField(blank=True)
    #슬러그
    slug = models.SlugField(default='garbage',allow_unicode=True,max_length=100)
    #썸네일
    thumb_nail = models.ImageField(default = 'default.png')

    def publish(self):
        self.save()

    def __str__(self):
        return self.scholar_name
    def my_slugify(self):
        self.slug = slugify(unidecode(self.scholar_name))

class Scholar_filter(models.Model):


    #####################
    KEYONGIDO='KEYNGIDO'
    SEOUL = 'SEOUL'
    BUSAN = 'BUSAN'
    DAEGOO = 'DAEGOO'
    INCHEON = 'INCHEON'
    DAEJUN = 'DAEJUN'
    ULSAN = 'ULSAN'
    KANGWONDO = 'KANGWONDO'
    CHUNGCHUNGBOOKDO = 'CHUNGCHUNGBOOKDO'
    CHUNGCHUNGNAMDO = 'CHUNGCHUNGNAMDO'
    JEOLABOOKDO='JEOLABOOKDO'
    JEOLANAMDO = 'JEOLANAMDO'
    KEYONGSANGBOOKDO = 'KEYONGSANGBOOKDO'
    KEYONGSANGNAMDO = 'KEYONGSANGNAMDO'
    SEJONG = 'SEJONG'
    JEJUDO = 'JEJUDO'


    Living_AREA_CHOICES=(
        (KEYONGIDO,'경기도'),
        (SEOUL,'서울특별시'),
        (BUSAN,'부산'),
        (DAEGOO,'대구'),
        (INCHEON,'인천'),
        (DAEJUN,'대전'),
        (ULSAN,'울산'),
        (KANGWONDO,'강원도'),
        (CHUNGCHUNGBOOKDO,'충청북도'),
        (CHUNGCHUNGNAMDO,'충청남도'),
        (JEOLABOOKDO,'전라북도'),
        (JEOLANAMDO,'전라남도'),
        (KEYONGSANGBOOKDO,'경상북도'),
        (KEYONGSANGNAMDO,'경상남도'),
        (SEJONG,'세종특별자치시'),
        (JEJUDO,'제주도')
    )
    ############################

    COMPLETION_SEMESTER_CHOICES=(
        (0,'아직 수료하지 않았습니다.'),
        (1,'1학기'),
        (2,'2학기'),
        (3,'3학기'),
        (4,'4학기'),
        (5,'5학기'),
        (6,'6학기'),
        (7,'7학기'),
        (8,'8학기'),
    )
    INCOME_LEVEL_CHOICES =(
        (0,'0분위'),
        (1,'1분위'),
        (2,'2분위'),
        (3,'3분위'),
        (4,'4분위'),
        (5,'5분위'),
        (6,'6분위'),
        (7,'7분위'),
        (8,'8분위'),
        (9,'9분위'),
        (10,'10분위'),
    )

    #id
    filter_id=models.OneToOneField(Scholar_content,on_delete=models.CASCADE)
    #성적
    filter_grade=models.FloatField(default=0)
    #수료학기
    filter_completion_semester=models.PositiveSmallIntegerField(choices=COMPLETION_SEMESTER_CHOICES,default=0)
    #소재지
    filter_living_area=models.CharField(max_length=200,choices= Living_AREA_CHOICES,null=True,default=None)
    #소득분위
    filter_income_level=models.PositiveSmallIntegerField(choices=INCOME_LEVEL_CHOICES,default=10,null=True)
    #교내(true)/교외(false)
    filter_is_our_college=models.BooleanField(default=False)
    #특이사항
    filter_uniqueness=models.TextField(blank=True,null=True)
    scholar_application_end=models.DateTimeField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if self.filter_id:
            self.scholar_application_end = self.filter_id.scholar_application_end
        super(Scholar_filter,self).save(*args,**kwargs)



class Uniqueness(models.Model):
    u_ID=models.OneToOneField(Scholar_filter,on_delete=models.CASCADE)
    #다문화가정
    u_1=models.BooleanField(default=False)
    #기초생활수급자
    u_2=models.BooleanField(default=False)
    #차상위계층
    u_3=models.BooleanField(default=False)
    #장애인
    u_4=models.BooleanField(default=False)
    #새터민
    u_5=models.BooleanField(default=False)
    #보훈대상자
    u_6=models.BooleanField(default=False)
    #조부모가정
    u_7=models.BooleanField(default=False)
    #다자녀
    u_8=models.BooleanField(default=False)
    #한부모
    u_9=models.BooleanField(default=False)
    #학생가장
    u_10=models.BooleanField(default=False)
    #농어촌자녀
    u_11=models.BooleanField(default=False)