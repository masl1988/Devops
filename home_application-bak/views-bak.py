# -*- coding: utf-8 -*-

from common.mymako import render_mako_context,render_json
from django.http import HttpResponse
from home_application.models import sum
from home_application.models import Author, Book
from home_application import models
from blueking.component.shortcuts import get_client_by_request

#def home(request):
#    """
#    首页
#    """
#    ip_list  = [1, 2, 3]
#    job_list = [{'id':1, 'name':u"zuoye1"},{'id':1, 'name':u"zuoye1"}]
#    countext = {'ip_list': ip_list, 'job_list': job_list}
#
#    return render_mako_context(request, '/home_application/home.html', countext)


def home(request):
    """
    首页
    """

    client = get_client_by_request(request)
    kwargs = {'app_id': 3}
    result = client.cc.get_app_host_list(kwargs)

    _ip_list = result.get('data', []) if result.get('result', False) else []
    ip_list = [_ip['InnerIP'] for _ip in _ip_list]


    job_resutl = client.job.get_task(kwargs)
    job_list = [{'id': str(i['id']), 'name': i['name']} for i in job_resutl.get('data', [])]


    countextip = {'ip_list': ip_list, 'job_list': job_list}
    return render_mako_context(request, 'home_application/home.html', countextip)


def excute_task(request):
    ip = request.GET.get('ip')
    job_id = request.GET.get('job_id')

    kwargs = {'app_id': 3,'ipList': ip , 'task_id': job_id}
    client = get_client_by_request(request)
    job = client.job.execute_task(kwargs)
    job_ins_id = job.get('data').get('taskInstanceId')
    return render_json({'job_ins_id': job_ins_id})


def excute(request):
    param1 = request.GET.get('param1')
    param2 = request.GET.get('param2')
    param = param1 + param2

    sum.objects.create(sum1=param1, sum2=param2, summ=param)
    return render_json({'param': param})


    ip_list  = [1, 2, 3]
#    job_list = [{'id':1, 'name':u"zuoye1"},{'id':1, 'name':u"zuoye1"}]
#    countext = {'ip_list': ip_list, 'job_list': job_list}
#    return render_mako_context(request, '/home_application/home.html', countext)







def home1(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home1.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def excute(request):
    param1 = request.GET.get('param1')
    param2 = request.GET.get('param2')
    param = param1 + param2

    sum.objects.create(sum1=param1, sum2=param2, summ=param)
    return render_json({'param': param})




def home1(request):
    lists = sum.objects.all()
    for list in lists:
        print list
        print list.sum1
        print list.sum2
        print list.summ

    countext = {'lists': lists}
    return render_mako_context(request, '/home_application/home1.html',countext)

def home2(request):
    summ = request.GET.get('sum')
    lists = sum.objects.filter(sum1=summ)

    countext = {'lists': lists}
    return render_mako_context(request, '/home_application/home1.html', countext)




#return HttpResponse(u'param1:%s, param2:%s' % (param1, param2))

#return HttpResponse('func show id:%s, param:%s, user:%s' % (id, param, username))