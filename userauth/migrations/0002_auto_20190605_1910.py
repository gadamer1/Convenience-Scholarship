# Generated by Django 2.0.13 on 2019-06-05 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUniqueness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_1', models.BooleanField(default=False)),
                ('u_2', models.BooleanField(default=False)),
                ('u_3', models.BooleanField(default=False)),
                ('u_4', models.BooleanField(default=False)),
                ('u_5', models.BooleanField(default=False)),
                ('u_6', models.BooleanField(default=False)),
                ('u_7', models.BooleanField(default=False)),
                ('u_8', models.BooleanField(default=False)),
                ('u_9', models.BooleanField(default=False)),
                ('u_10', models.BooleanField(default=False)),
                ('u_11', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='uniqueness',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useruniqueness',
            name='u_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.Profile'),
        ),
    ]
