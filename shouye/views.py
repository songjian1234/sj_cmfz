from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

import redis
redis = redis.Redis(host='127.0.0.1', port=6379)

from django.views.decorators.csrf import csrf_exempt

from sj_cmfz.settings import API_KEY
from utils.random_code import Yanzheng
from utils.send_mess import YunPian
from utils.shoujigeshi import Shouji


def shouye(request):
    return render(request,'shouye.html')


def login_form(request):
    return render(request, "login.html")


@csrf_exempt
def get_code(request):
    """
    接受前端发送的ajax请求并为手机号发送验证码
    :param request: 用户输入的数据号
    :return: None
    """

    mobile = request.POST.get("mobile")

    # 获取手机号有没有对应的验证码 查看验证码是否在120S内  如果在  提示验证码已经发送
    # value = redis.get("18500230996_1")  如果返回的值存在  代表120s之内还不能发送
    ww = mobile+'1'
    phon = redis.get(ww)
    if phon:
        return HttpResponse('aaa')

    # 判断手机号是否存在  正则验证是否合法
    # 判断手机号是否正确
    phone = Shouji()
    phone = phone.phonecheck(mobile)
    if phone:
        code = Yanzheng(6, False)
        a = code.code()
        print(a)
        yun_pian = YunPian(API_KEY)
        yun_pian.send_message(mobile, a)
        # 将手机号与对应的验证码存入redis  防止无限制发送
        mo = mobile+'1'
        redis.set(mo,a,ex=120)

        # redis.set("18500230996_1", "666666", 120S)
        # 保证验证码的有效期
        # redis.set("18500230996_2", "666666", 600s)
        redis.set(mobile, a, ex=600)
        print("发送成功")
        return HttpResponse("ok")
    else:
        return HttpResponse("no")


def check_user(request):
    """
    用户登录信息校验的视图
    :param request: 表单数据
    :return:
    """
    mobile = request.GET.get('mobile')
    code = request.GET.get('code')
    print(mobile, str(code))
    # 校验信息是否合法
    if code.isdigit():
        # 验证码是否在有效期内  使用redis
        # redis.get("18500230996_2")
        co = redis.get(mobile)
        co = str(co)

        if str(co[2:-1]) == code:
            return HttpResponse('ok')
    return HttpResponse('no')
