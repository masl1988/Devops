# -*- coding: utf-8 -*-
import time

from common.mymako import render_mako_context,render_json
from home_application.models import sum
from django.http import HttpResponse
#from home_application import models
from blueking.component.shortcuts import get_client_by_request


def index(request):
    """
    乘法运算
    """
    return render_mako_context(request, '/home_application/index.html')

def create_db(request):
    """
    获取前端index.html传递的输入变量并写入数据库中
    """
    input1 = request.GET.get('input1')
    input2 = request.GET.get('input2')
    input_sum = int(input1) * int(input2)

    sum.objects.create(sum1=input1, sum2=input2, summ=input_sum)
    return render_json({'input_sum': input_sum})

def tasks(request):
    """
    作业平台
    """
    client = get_client_by_request(request)
#指定paas平台的业务app_id的数值
    app_id = {'app_id': 3}

#指定result 获取app_id为3的主机列表
    result = client.cc.get_app_host_list(app_id)

# 使用python处理获取到的数据
    _ip_list = result.get('data', []) if result.get('result', False) else []
    ip_list = [_ip['InnerIP'] for _ip in _ip_list]

    job_resutl = client.job.get_task(app_id)
    job_list = [{'id': str(i['id']), 'name': i['name']} for i in job_resutl.get('data', [])]

# 定义字典并传递数值到前端
    countext = {'ip_list': ip_list, 'job_list': job_list}
    return render_mako_context(request, '/home_application/tasks.html',countext)


def tasks_job(request):

    select1 = request.GET.get('select1')
    select2 = request.GET.get('select2')

    client = get_client_by_request(request)

    kwargs = {'app_id': 3,'ipList': select1 , 'task_id': select2}
    job = client.job.execute_task(kwargs)
    job_ins_id = job.get('data').get('taskInstanceId')

#time.sleep(6)
    kwargs1 = {'task_instance_id': job_ins_id}
    #print kwargs1

# 通过 client.job.get_task_result的API获取
    job_result = client.job.get_task_result(kwargs1)
    #print job_result

    job_status = job_result['data']['taskInstance']['status']
    #print job_status
#获取到的数据存储至数据库
    sum.objects.create(sum1=select1, sum2=select2, summ=job_status)

# 通过client.job.get_task_ip_log的API去查询任务详情
    job_log_result = client.job.get_task_ip_log(kwargs1)
    print job_log_result
    job_log_ip = job_log_result['data'][0]['stepAnalyseResult'][0]['ipLogContent'][0]['ip']
    job_log_Text = job_log_result['data'][0]['stepAnalyseResult'][0]['resultTypeText']


    #print '*'*100
    #print job_log_ip
    #print job_log_Text

    job_message = job_log_ip + job_log_Text
    #job_list = sum.objects.all()
    #print job_list
    #print job_message
    return render_json({'job_log_ip': job_log_ip, 'job_log_Text': job_log_Text})


def tasks_test(request):
    ip_list = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
    job_list = [{'id':1, 'name':u"作业1"},{'id':2, 'name':u"作业二"}]
    countext = {'ip_list': ip_list, 'job_list': job_list}
    return render_mako_context(request, '/home_application/tasks.html', countext)


def search(request):
    """
    查询搜索
    """
    return render_mako_context(request, '/home_application/search.html')
