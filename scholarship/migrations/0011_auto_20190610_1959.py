# Generated by Django 2.0.13 on 2019-06-10 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0010_scholar_filter_scholar_application_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniqueness',
            name='u_ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='uniqueness', to='scholarship.Scholar_filter'),
        ),
    ]