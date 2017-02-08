# -*- coding: utf-8 -*-

from common.mymako import render_mako_context,render_json
from django.http import HttpResponse
from home_application.models import sum



def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


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

#return HttpResponse(u'param1:%s, param2:%s' % (param1, param2))

#return HttpResponse('func show id:%s, param:%s, user:%s' % (id, param, username))