import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def first_pag(request):
    """
    为前台系统的首页 专辑页  文章页提供数据支持
    :param request:
    :return:
    """

    user_id = request.GET.get("uid")
    type = request.GET.get("type")
    sub_type = request.GET.get("sub_type")

    if not user_id:
        data = {
            'status': 401,
            'msg': "用户未登陆"
        }
        return HttpResponse(json.dumps(data))

    # 代表访问的事首页
    if type == "all":
        # 查询首页所需的数据并按规定的格式响应回去
        # 轮播图  专辑  文章
        pass
    elif type == "wen":
        # 代表范文的是专辑 查询专辑的信息响应回去
        pass
    elif type == "si":
        if sub_type == "ssyj":
            # 查询属于上师言教的文章
            pass
        else:
            # 查询属于显密法要的文章
            pass

    user_json = {
        "name": "marry",
        "age": 18,
        "bir": "2012-12-12"
    }

    return HttpResponse(json.dumps(user_json))
