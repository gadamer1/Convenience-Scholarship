from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from .models import Scholar_content,Scholar_filter,Uniqueness
from django.db.models import Q
# Create your views here.


def main(request):
    page = request.GET.get('page','1')
    page = int(page)
    scholars = Scholar_content.objects.all().order_by('scholar_application_end').reverse()
    num=5
    paginator = Paginator(scholars,num)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    #if page's number smaller than 5
    if paginator.num_pages < num:
        num= paginator.num_pages
    
    start_index = 1
    end_index = paginator.num_pages
    if p.number>5:
        start_index = p.number-5
    if paginator.num_pages > p.number+5:
        end_index = p.number+5
    
    page_range = range(start_index,end_index+1)
    return render(request, 'scholarship/main.html', {'scholars': p, 'page_range': page_range,
    'page_start_index':start_index,'page_end_index':end_index})

def scholarship_detail(request,scholar_slug):
    scholar = Scholar_content.objects.get(slug=scholar_slug)
    
    return render(request,'scholarship/detail.html',{'scholar':scholar})

@login_required(login_url ='login/login')
def scholarship_my_scholar(request):
    instances = Scholar_filter.objects.exclude(Q(filter_grade__gt=request.user.profile.user_grade),
    Q(filter_completion_semester__gt=request.user.profile.user_completion_semester),
    Q(filter_income_level__lt=request.user.profile.user_income_level)).order_by('scholar_application_end').reverse()
    scholars={} 
    scholars=list(scholars)
    for instance in instances:
        scholars += list(Scholar_content.objects.filter(scholar_name=instance.filter_id.scholar_name))

    page = request.GET.get('page','1')
    page = int(page)
    num=5
    paginator = Paginator(scholars,num)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    #if page's number smaller than 5
    if paginator.num_pages < num:
        num= paginator.num_pages
    
    start_index = 1
    end_index = paginator.num_pages
    if p.number>5:
        start_index = p.number-5
    if paginator.num_pages > p.number+5:
        end_index = p.number+5
    
    page_range = range(start_index,end_index+1)
    return render(request, 'scholarship/my_scholar.html', {'scholars': p, 'page_range': page_range,
    'page_start_index':start_index,'page_end_index':end_index})
