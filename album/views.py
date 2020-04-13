import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from mutagen.mp3 import MP3

# Create your views here.
from shouye.models import TAlbum, TChapter


import uuid,os
def generateUUID(filename):    # 创建唯一的文件名
    id = str(uuid.uuid4())
    extend = os.path.splitext(filename)[1]
    return id+extend


def getAllAlbum(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = TAlbum.objects.all().order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, TAlbum):
            return {
                "author": u.author,
                "url": str(u.url),
                "name": u.name,
                "date": u.date.strftime('%Y-%m-%d'),
                "id": u.id,
                "announcer": u.announcer,
                "score": u.score,
                "num": u.num,
                "content": u.content,
            }

    data = json.dumps(page_data, default=myDefault)
    print(data)

    return HttpResponse(data)


def getChapterByAlbumId(request):
    album_Id = request.GET.get('albumId')
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = TChapter.objects.all().filter(t_id=album_Id).order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, TChapter):
            return {
                "name": u.name,
                "duration": u.duration,
                "id": u.id,
                "size": u.size,
                "url": str(u.url),
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


@csrf_exempt
def editAlbum(request):
    oper = request.POST.get('oper')
    if oper == 'add':
        print('添加')
    elif oper =='edit':
        name = request.POST.get('name')
        score = request.POST.get('score')
        id = request.POST.get('id')
        author = request.POST.get('author')
        announcer = request.POST.get('announcer')
        num = request.POST.get('num')
        content = request.POST.get('content')
        print(id, name, score,author,announcer,content,num)
        emp = TAlbum.objects.get(id=id)
        emp.name = name
        emp.score = score
        emp.author = author
        emp.announcer = announcer
        emp.content = content
        emp.num = num
        emp.save()
    elif oper == 'del':
        id = request.POST.get('id')
        TAlbum.objects.get(pk=id).delete()
    return HttpResponse('ok')


@csrf_exempt
def add_chapter(request):
    idd = request.POST.get('idd')
    print(idd)
    name = request.POST.get('yinpin_title')
    audio = request.FILES.get("url")
    print(audio)
    # 音频大小
    audio_1 = audio.size
    # 音频时长
    audio_mp3 = MP3(audio)
    duration = audio_mp3.info.length
    print(name,audio,audio_mp3)
    TChapter.objects.create(name=name,size=audio_1,duration=duration,url=audio,t_id=idd)

    return HttpResponse()


@csrf_exempt
def add_album(request):
    album_title = request.POST.get("album_title")
    album_name = request.POST.get('album_name')
    album_score = request.POST.get('album_score')
    album_author = request.POST.get('album_author')
    album_announcer = request.POST.get('album_announcer')
    album_content = request.POST.get('album_content')
    album_num = request.POST.get('album_num')
    pic = request.FILES.get('pic')
    pic.name = generateUUID(pic.name)
    print(album_title, album_name,album_score,album_author,album_announcer,album_content,album_num, pic)
    TAlbum.objects.create(url=pic, name=album_name, score=album_score, author=album_author,announcer=album_announcer,num=album_num,content=album_content)
    return HttpResponse('ok')


@csrf_exempt
def editAlbum_1(request):
    oper = request.POST.get('oper')
    if oper == 'edit':
        id = request.POST.get('id')
        name = request.POST.get('name')
        emp = TChapter.objects.get(id=id)
        emp.name = name
        emp.save()
    elif oper == 'del':
        id = request.POST.get('id')
        TChapter.objects.get(pk=id).delete()
    return HttpResponse('ok')
