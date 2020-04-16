import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from shouye.models import TPhoto, TAlbum, TArticle, TChapter, TUser


def first_pag(request):
    """
    为前台系统的首页 专辑页  文章页提供数据支持
    :param request:
    :return:
    """

    user_id = request.GET.get("uid")
    type = request.GET.get("type")
    sub_type = request.GET.get("sub_type")
    data = {}

    if not user_id:
        data = {
            'status': 401,
            'msg': "用户未登陆"
        }
        return HttpResponse(json.dumps(data))

    banner = TPhoto.objects.all()
    album = TAlbum.objects.all()
    artical = TArticle.objects.all()
    headers = []
    body = []

    # 代表访问的事首页
    if type == "all":
        # 查询首页所需的数据并按规定的格式响应回去
        # 轮播图  专辑  文章
        for i in banner:
            headers.append({
                'thumbnail': 'http://127.0.0.1:8000/static/' + str(i.url),
                'desc': i.describe_1,
                'id': i.id,
            })
        for i in album:
            body.append({
                'thumbnail': 'http://127.0.0.1:8000/static/' + str(i.url),
                'title': i.name,
                'author': i.author,
                'type': 0,
                'set_count': i.num,
                'create_date': i.date.strftime('%Y-%m-%d'),
            })
        for i in artical:
            body.append({
                'thumbnail': '',
                'title': i.url,
                'author': '',
                'type': 1,
                'create_date': i.data.strftime('%Y-%m-%d'),
            })
        data['header'] = headers
        data['body'] = body
    elif type == "wen":
        # 代表范文的是专辑 查询专辑的信息响应回去
        for i in album:
            body.append({
                'thumbnail': 'http://127.0.0.1:8000/static/' + str(i.url),
                'title': i.name,
                'author': i.author,
                'type': 0,
                'set_count': i.num,
                'create_date': i.date.strftime('%Y-%m-%d'),
            })
        data['body'] = body
    elif type == "si":
        if sub_type == "ssyj":
            # 查询属于上师言教的文章
            a = 1
            artical = TArticle.objects.filter(t_url=a)
            for i in artical:
                body.append({
                    'thumbnail': 'http://127.0.0.1:8000/static/' + str(i.url),
                    'title': i.name,
                    'author': '',
                    'type': 1,
                    'create_date': i.data.strftime('%Y-%m-%d'),
                })
        if sub_type == 'xmfy':
            a = 2
            artical = TArticle.objects.filter(t_url=a)
            print(artical)
            for i in artical:
                body.append({
                    'thumbnail': 'http://127.0.0.1:8000/static/' + str(i.url),
                    'title': i.name,
                    'author': '',
                    'type': 1,
                    'create_date': i.data.strftime('%Y-%m-%d'),
                })
        data['body'] = body


    return HttpResponse(json.dumps(data))


def wen(request):
    uid = request.GET.get("uid")
    id = request.GET.get("id")
    print(uid,id)
    data = {}
    if uid:
        album = TAlbum.objects.filter(id=id)
        if album:
            album = album[0]
            introduction = {
                'thumbnail':'http://127.0.0.1:8000/static/' + str(album.url),
                'title':album.name,
                'score':album.score,
                'author':album.author,
                'broadcast':album.announcer,
                'set_count':album.num,
                'brief':album.content,
                'create_date': album.date.strftime('%Y-%m-%d'),
            }
            chapter = TChapter.objects.filter(t_id=album.id)
            a = []
            for i in chapter:
                a.append({
                    'title':i.name,
                    'download_url':'http://127.0.0.1:8000/static/'+str(i.url),
                    'size':i.size,
                    'duration':i.duration
                })
            data['introduction']=introduction
            data['list']=a
    return JsonResponse(data)

@csrf_exempt
def regist(request):
    password = request.POST.get("password")
    phone = request.POST.get("phone")
    user = TUser.objects.filter(phone=phone)
    data = {}
    print(password,phone)
    if user:
        data['errno']='-200'
        data['error_msg']='该手机号已经存在'
    else:
        if password and phone:
            user = TUser.objects.create(pwd=password,phone=phone)
            id = TUser.objects.get(phone=phone)
            data['uid']=id.id
            data['password']=password
            data['phone']=phone
    return JsonResponse(data)

@csrf_exempt
def modify(request):
    uid = request.POST.get("uid")
    gender = request.POST.get("gender")
    photo = request.FILES.get("photo")
    location = request.POST.get("location")
    description = request.POST.get("description")
    nickname = request.POST.get("nickname")
    province = request.POST.get("province")
    city = request.POST.get("city")
    password = request.POST.get("password")
    data = {}
    user = TUser.objects.filter(id=uid)[0]
    if user:
        if password:
            user.pwd = password
        if city:
            user.address = city
        if nickname:
            user.name = nickname
        if description:
            user.autograph = description
        if gender:
            if gender == 'm':
                user.sex = '1'
            if gender=='f':
                user.sex = '2'
        user.save()
        data['password'] = user.pwd
        data['farmington'] = ''
        data['uid'] = user.id
        data['nickname'] = user.name
        data['gender'] = user.gender
        data['photo'] = 'http://127.0.0.1:8000/static/'+str(user.photo)
        data['location'] = ''
        data['province'] = ''
        data['city'] = user.address
        data['description'] = user.autograph
        data['phone'] = user.phone
    else:
        data['errno']='-200'
        data['error_msg']='用户ID不存在'
    return JsonResponse(data)
