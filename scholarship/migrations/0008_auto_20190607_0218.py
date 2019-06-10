# Generated by Django 2.0.13 on 2019-06-06 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0007_auto_20190607_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholar_filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_grade', models.FloatField(default=4.5)),
                ('filter_completion_semester', models.PositiveSmallIntegerField(choices=[(0, '아직 수료하지 않았습니다.'), (1, '1학기'), (2, '2학기'), (3, '3학기'), (4, '4학기'), (5, '5학기'), (6, '6학기'), (7, '7학기'), (8, '8학기')], default=0)),
                ('filter_living_area', models.CharField(choices=[('KEYNGIDO', '경기도'), ('SEOUL', '서울특별시'), ('BUSAN', '부산'), ('DAEGOO', '대구'), ('INCHEON', '인천'), ('DAEJUN', '대전'), ('ULSAN', '울산'), ('KANGWONDO', '강원도'), ('CHUNGCHUNGBOOKDO', '충청북도'), ('CHUNGCHUNGNAMDO', '충청남도'), ('JEOLABOOKDO', '전라북도'), ('JEOLANAMDO', '전라남도'), ('KEYONGSANGBOOKDO', '경상북도'), ('KEYONGSANGNAMDO', '경상남도'), ('SEJONG', '세종특별자치시'), ('JEJUDO', '제주도')], default=None, max_length=200, null=True)),
                ('filter_income_level', models.PositiveSmallIntegerField(choices=[(0, '0분위'), (1, '1분위'), (2, '2분위'), (3, '3분위'), (4, '4분위'), (5, '5분위'), (6, '6분위'), (7, '7분위'), (8, '8분위'), (9, '9분위'), (10, '10분위')], default=10, null=True)),
                ('filter_is_our_college', models.BooleanField(default=False)),
                ('filter_uniqueness', models.TextField(blank=True, null=True)),
                ('filter_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scholarship.Scholar_content')),
            ],
        ),
        migrations.RemoveField(
            model_name='scholar_fliter',
            name='filter_id',
        ),
        migrations.DeleteModel(
            name='Scholar_fliter',
        ),
    ]
