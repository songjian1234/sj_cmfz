import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from shouye.models import TPhoto


def get_all_banner(request):
    """
    获取所有轮播图的相关信息并转换成json响应的前端
    :param request:
    :return:
    """
    rows = request.GET.get('rows')
    page = request.GET.get('page')

    emp_list = TPhoto.objects.all().order_by('id')

    all_page = Paginator(emp_list, rows)
    # 获取分页后第一页的对象
    try:
        page_obj = Paginator(emp_list, rows).page(page).object_list
    except:
        page_obj = Paginator(emp_list, rows).page(str(int(page) - 1)).object_list
    page_data = {
        "page": page,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": list(page_obj)
    }

    # 对象序列化
    def myDefault(u):
        if isinstance(u, TPhoto):
            return {"id": u.pk,
                    "url": u.url,
                    "describe": u.describe_1,
                    "show": u.show_1,}
    data = json.dumps(page_data, default=myDefault)
    print(data)
    return HttpResponse(data)


# 添加数据
@csrf_exempt
def add_banner(request):
    title = request.POST.get("title")
    status = request.POST.get('status')
    pic = request.FILES.get('pic')
    print(title, status, pic)
    TPhoto.objects.create(url=pic, show_1=status, describe_1=title,)
    return HttpResponse('ok')


@csrf_exempt
def data_oper(request):
    '''
    根据当前不同的操作 增/删/改 进行区分处理
    :param request: oper参数 add/edit/del
    :return:
    '''
    oper = request.POST.get('oper')
    print(oper)

    if oper == 'edit': # 修改
        info = request.POST.get('describe')
        status = request.POST.get('show')
        id = request.POST.get('id')
        print(id,info,status)
        emp = TPhoto.objects.get(id=id)
        emp.describe_1 = info
        emp.show_1 = status
        emp.save()
    elif oper == 'del' : # 删除
        id = request.POST.get('id')
        TPhoto.objects.get(pk=id).delete()
    return HttpResponse('ok')



