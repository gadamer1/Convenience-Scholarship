# Generated by Django 2.0.13 on 2019-06-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20190605_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_grade',
            field=models.FloatField(default=4.5, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_living_area',
            field=models.CharField(choices=[('KEYNGIDO', '경기도'), ('SEOUL', '서울특별시'), ('BUSAN', '부산'), ('DAEGOO', '대구'), ('INCHEON', '인천'), ('DAEJUN', '대전'), ('ULSAN', '울산'), ('KANGWONDO', '강원도'), ('CHUNGCHUNGBOOKDO', '충청북도'), ('CHUNGCHUNGNAMDO', '충청남도'), ('JEOLABOOKDO', '전라북도'), ('JEOLANAMDO', '전라남도'), ('KEYONGSANGBOOKDO', '경상북도'), ('KEYONGSANGNAMDO', '경상남도'), ('SEJONG', '세종특별자치시'), ('JEJUDO', '제주도')], default='SEOUL', max_length=200),
        ),
    ]
