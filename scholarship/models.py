from django.db import models
from unidecode import unidecode
from django.utils.text import slugify
from random import randint
# Create your models here.


class Scholar_content(models.Model):

    @staticmethod
    def randomtag():
        return str(randint(9,11))


    #장학이름
    scholar_name=models.CharField(max_length=200,primary_key=True,verbose_name='장학이름')
    #장학혜택
    scholar_reward=models.TextField(blank=True,verbose_name='장학혜택')
    #제출서류
    scholar_needs=models.TextField(blank=True,verbose_name='제출서류')
    #접수방법
    scholar_howto=models.TextField(blank=True,verbose_name='접수방법')
    #장학 문의 번호
    scholar_qna=models.TextField(blank=True,verbose_name='장학문의번호')
    #선발인원
    scholar_recruitment_num=models.PositiveIntegerField(verbose_name='선발인원')
    #모집기간
    scholar_application_start=models.DateTimeField(blank=True,null=True,verbose_name='제출기간 시작')
    scholar_application_end = models.DateTimeField(blank=True,null=True,verbose_name='제출기간 마지막')
    #장학재단명
    scholar_foundation_name=models.CharField(max_length=200,verbose_name='장학재단이름')
    #선발대상
    scholar_who_draft=models.TextField(blank=True,verbose_name='선발대상')
    #슬러그
    slug = models.SlugField(default='garbage',allow_unicode=True,max_length=100,verbose_name='슬러그')
    #썸네일
    thumb_nail = models.ImageField(default = 'default.png',verbose_name='썸네일')
    #양식
    form_file = models.FileField(verbose_name='양식업로드',null=True)

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
    filter_id=models.OneToOneField(Scholar_content,on_delete=models.CASCADE,verbose_name='아이디')
    #성적
    filter_grade=models.FloatField(default=0,verbose_name='성적')
    #수료학기
    filter_completion_semester=models.PositiveSmallIntegerField(choices=COMPLETION_SEMESTER_CHOICES,default=0,verbose_name='수료학기')
    #소재지
    filter_living_area=models.CharField(max_length=200,choices= Living_AREA_CHOICES,null=True,default=None,verbose_name='소재지')
    #소득분위
    filter_income_level=models.PositiveSmallIntegerField(choices=INCOME_LEVEL_CHOICES,default=10,null=True,verbose_name='소득분위')
    #교내(true)/교외(false)
    filter_is_our_college=models.BooleanField(default=False,verbose_name='교내/교외')
    #특이사항
    filter_uniqueness=models.TextField(blank=True,null=True,verbose_name='특이사항')
    scholar_application_end=models.DateTimeField(blank=True,null=True,verbose_name='자동생성 제출기간 마지막')

    def save(self,*args,**kwargs):
        if self.filter_id:
            self.scholar_application_end = self.filter_id.scholar_application_end
        super(Scholar_filter,self).save(*args,**kwargs)



class Uniqueness(models.Model):
    u_ID=models.OneToOneField(Scholar_filter,on_delete=models.CASCADE,related_name='uniqueness')
    #다문화가정
    u_1=models.BooleanField(default=False,verbose_name='다문화가정')
    #기초생활수급
    u_2=models.BooleanField(default=False,verbose_name='기초생활수급자')
    #차상위계층
    u_3=models.BooleanField(default=False,verbose_name='차상위계층')
    #장애인
    u_4=models.BooleanField(default=False,verbose_name='장애인')
    #새터민
    u_5=models.BooleanField(default=False,verbose_name='새터민')
    #보훈대상자
    u_6=models.BooleanField(default=False,verbose_name='보훈대상자')
    #조부모가정
    u_7=models.BooleanField(default=False,verbose_name='조부모가정')
    #다자녀
    u_8=models.BooleanField(default=False,verbose_name='다자녀')
    #한부모
    u_9=models.BooleanField(default=False,verbose_name='한부모')
    #학생가장
    u_10=models.BooleanField(default=False,verbose_name='학생가장')
    #농어촌자녀
    u_11=models.BooleanField(default=False,verbose_name='농어촌자녀')