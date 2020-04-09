import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from shouye.models import TUser


import uuid,os
def generateUUID(filename):    # 创建唯一的文件名
    id = str(uuid.uuid4())
    extend = os.path.splitext(filename)[1]
    print(id+extend)
    return id+extend


def my_default(e):
    if isinstance(e, TUser):
        return {'id': e.id, 'name': e.name, 'pwd': e.pwd, 'info': e.autograph, 'phone': e.phone, 'addr': e.address,
                'url': str(e.photo), 'gender': e.gender, 'add_time': e.spare.strftime('%Y-%m-%d')}


def query_all(request):
    rowNum = request.GET.get('rows')
    pageNum = request.GET.get("page")
    emps = TUser.objects.all()
    print(emps)
    # 创建分页器对象
    pgntor = Paginator(emps, rowNum)
    pg = pgntor.page(pageNum)  # 创建当前page对象
    # print(list(pg),'28hang') # 获取当前页中的所有数据对象
    print(pg)
    # 构建此时json数据
    re_data = {"page": pageNum,  # 当前页号
               "total": pgntor.num_pages,  # 总页数
               "records": pgntor.count,  # 总条目数
               "rows": list(pg)  # 使用list()可以直接获取当前上所有model对象
               }
    json_str = json.dumps(re_data, default=my_default)
    print(json_str)
    return HttpResponse(json_str)


@csrf_exempt
def add_banner(request):
    """
    添加轮播图的方法
    :param request:
    :return:
    """
    info = request.POST.get('info')
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    phone = request.POST.get('phone')
    addr = request.POST.get('addr')
    gender = request.POST.get('gender')
    url = request.FILES.get("pic")
    url.name = generateUUID(url.name)
    print(info, name, url, gender, phone, pwd, addr)
    TUser.objects.create(name=name, pwd=pwd, phone=phone, address=addr, photo=url, autograph=info, gender=gender)
    return HttpResponse("ok")


@csrf_exempt
def data_oper(request):
    '''
    根据当前不同的操作 增/删/改 进行区分处理
    :param request: oper参数 add/edit/del
    :return:
    '''
    oper = request.POST.get('oper')
    if oper == 'edit':  # 修改
        info = request.POST.get('info')
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        id = request.POST.get('id')
        phone = request.POST.get('phone')
        address = request.POST.get('addr')
        emp = TUser.objects.get(id=id)
        emp.autograph = info
        emp.phone = phone
        emp.pwd = pwd
        emp.address = address
        emp.name = name
        emp.save()
    elif oper == 'del':  # 删除
        id = request.POST.get('id')
        TUser.objects.get(pk=id).delete()
    return HttpResponse('ok')
