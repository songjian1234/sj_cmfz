import json
import os

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

from article.models import Pic
from shouye.models import TArticle


def load_kind(request):
    return render(request, "kindeditor.html")


def getALLArticle(request):
    """
    获取所有文章的相关信息并转换成json响应的前端
    :param request:
    :return:
    """
    rows = request.GET.get('rows')
    page = request.GET.get('page')

    emp_list = TArticle.objects.all().order_by('id')

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
        if isinstance(u, TArticle):
            return {"id": u.pk,
                    "name": u.name,
                    "data": u.data.strftime('%Y-%m-%d'),
                    "content": u.content,
                    "url": u.url,
                    "t_url": u.t_url,
                    }
    data = json.dumps(page_data, default=myDefault)
    print(data)
    return HttpResponse(data)


@xframe_options_sameorigin  # 允许页面嵌套时发起访问
@csrf_exempt
def upload_img(request):
    """
    富文本上传图片所使用的的方法
    :param request: 文件
    :return:{"error":0,"url":"\/ke4\/attached\/W020091124524510014093.jpg"}
    图片所在的服务器路径
    """

    file = request.FILES.get("imgFile")
    print(file)
    print(str(file))

    if file:
        # 获取图片所在的服务的全路径
        img_url = request.scheme + "://" + request.get_host() + "/static/img/" + str(file)
        print(img_url)
        result = {"error": 0, "url": img_url}
        Pic.objects.create(img=file)
    else:
        result = {"error": 1, "url": "上传失败"}
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_all_img(request):
    """
    获取所有图片的方法
    :param request:
    :return:
    """
    # 找到图片所在的目录  方便进行回显
    pic_dir = request.scheme + "://" + request.get_host() + '/'

    pic_dir = pic_dir+'static/'
    print(pic_dir)
    pic_list = Pic.objects.all()

    rows = []

    for i in list(pic_list):
        # 获取图片的后缀
        path, pic_suffix = os.path.splitext(i.img.url)
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": i.img.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffix,
            "filename": i.img.name,
            "datetime": str(timezone.now())
        })

    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_dir,
        "total_count": len(pic_list),
        "file_list": rows

    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def add_article(request):
    """
    添加文章的方法
    :param request:
    :return:
    """

    category = request.GET.get('category')
    title = request.GET.get('title')
    content = request.GET.get('content')
    name = request.GET.get('name')
    print(category, title, content,name)

    # 可以根据获取到的值进行保存
    TArticle.objects.create(name=name,url=title,content=content,t_url=category)

    return HttpResponse()


def edit_article(request):
    category = request.GET.get('category_1')
    id = request.GET.get('id_111')
    title = request.GET.get('title_1')
    content = request.GET.get('content_1')
    name = request.GET.get('name_1')
    print(category,id,title,content,name)
    emp = TArticle.objects.filter(id=id)[0]
    emp.url = title
    emp.name = name
    emp.content = content
    emp.t_url = category
    emp.save()
    return HttpResponse('ok')


def del_article(request):
    id = request.GET.get('id')
    TArticle.objects.get(id=id).delete()
    return HttpResponse('ok')
