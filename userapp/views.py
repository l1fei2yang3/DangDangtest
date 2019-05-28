import hashlib
import random
import string
from datetime import datetime

from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from userapp.captcha.image import ImageCaptcha
from userapp.models import TUser, Confirm_string


def login(request):
    flag=request.GET.get("flag")
    request.session["ffff"]=flag
    fla = request.session.get("fla")
    jiesuan = request.session.get("jiesuan")
    print(fla,flag,'15行的fla')
    txtUsername = request.COOKIES.get("txtUsername")
    txtpwd = request.COOKIES.get("txtPassword")
    re_name = request.session.get("re_name")
    re_pwd = request.session.get("re_pwd")
    print(re_name,re_pwd,'18行')
    exit = request.session.get("exit")
    log = request.session.get("log")
    print(txtpwd,txtUsername,'15行')
    if exit!="1":
        # if log is None:
        #     del request.session["log"]
        log=request.session.get("log")
        if txtUsername:
            txtuser=txtUsername.encode("latin-1").decode("utf-8")
            # passw = request.session.get("passw")
            passw = TUser.objects.filter(email=txtuser)[0].password
            status = TUser.objects.filter(email=txtuser)[0].status
            print(status,'33行')
            if status == 1:
                pas = check_password(txtpwd,passw)
                print(pas,passw,'27行能不能')
                if pas:
                    print("24行走不")
                    request.session["log"] = txtUsername
                    request.session["login"] = "ok"
                    if flag == "car":
                        print("48行执行没")
                        return redirect("shopapp:car")
                    return redirect("indexapp:index")
            elif re_name and re_pwd:
                print("39行测试能不能走")
                result=TUser.objects.filter(email=re_name,password=re_pwd)
                if result:
                    request.session["log"] = re_name
                    request.session["login"] = "ok"
                    if fla == "car":
                        return redirect("shopapp:car")
                    if flag == "car":
                        print("48行执行没")
                        return redirect("shopapp:car")
                    return redirect("indexapp:index")
            else:
                txtPassword=request.session.get("txtPassword")
                txtUsername=request.session.get("txtUsername")
                passw=request.session.get("passw")
                pas = check_password(txtPassword, passw)
                if status == 1:
                    if pas:
                        request.session["log"] = txtUsername
                        print(txtUsername,'29行txt')
                        request.session["login"] = "ok"
                        if flag == "car":
                            print("48行执行没")
                            return redirect("shopapp:car")
                        else:
                            return redirect("indexapp:index")
    # if log is None:
    #     return render(request,'userapp/login.html')
    elif txtUsername and txtpwd:
        txtuser = txtUsername.encode("latin-1").decode("utf-8")
        # passw = request.session.get("passw")
        passw = TUser.objects.filter(email=txtuser)[0].password
        status = TUser.objects.filter(email=txtuser)[0].status
        pas = check_password(txtpwd, passw)
        print(pas, passw, '27行能不能')
        if status == 1:
            if pas:
                print("24行走不")
                request.session["log"] = txtUsername
                print(txtUsername, '29行txt')
                request.session["login"] = "ok"
                if flag == "car":
                    print("48行执行没")
                    return redirect("shopapp:car")
                return redirect("indexapp:index")
    else:
        del request.session["exit"]
    return render(request,'userapp/login.html',{"flag":flag})

def loginlogic(request):
    txtUsername=request.POST.get("txtUsername")
    txtPassword=request.POST.get("txtPassword")
    request.session["txtUsername"] = txtUsername
    request.session["txtPassword"] = txtPassword
    print(txtUsername,txtPassword,"24行")
    passw = TUser.objects.filter(email=txtUsername)[0].password
    request.session["passw"]=passw
    txtPassword = check_password(txtPassword, passw)
    print(txtPassword,'29行')
    if txtPassword:
        # result=TUser.objects.filter(email=txtUsername,password=txtPassword)
        # if result:
        return HttpResponse("1")
    return HttpResponse("0")
def loginjump(request):
    code = request.session.get("code")
    stat = request.session.get("stat")
    ffff = request.session.get("ffff")
    jiesuan = request.session.get("jiesuan")
    print(stat, '14行stat')
    txtUsername=request.POST.get("txtUsername")
    txtPassword=request.POST.get("txtPassword")
    print(txtUsername,txtPassword,'34行')
    autologin=request.POST.get("autologin")#cookie
    print(autologin,'65行coonkie')
    txt_vcode=request.POST.get("txt_vcode")
    print(txt_vcode,'39行')
    passw=TUser.objects.filter(email=txtUsername)[0].password
    status=TUser.objects.filter(email=txtUsername)[0].status
    txtpwd = check_password(txtPassword,passw)
    print(txtpwd,'45行')
    # result=TUser.objects.filter(email=txtUsername,password=txtPassword)
    if txt_vcode.upper() == code.upper():
        if txtpwd and stat is None:
            if status=="1":
                print(status,'130行')
                if ffff == "car":
                    request.session["log"] = txtUsername
                    request.session["login"] = "ok"
                    return redirect("shopapp:car")
                elif jiesuan:
                    del request.session["jiesuan"]
                    print("13448行执行没")
                    request.session["log"] = txtUsername
                    request.session["login"] = "ok"
                    return redirect("shopapp:indent")
                elif ffff=="cars":
                    request.session["log"] = txtUsername
                    request.session["login"] = "ok"
                    return redirect("shopapp:car")
                res=redirect("indexapp:index")
                request.session["log"] = txtUsername
                request.session["login"]="ok"
                if autologin:
                    res.set_cookie("txtUsername", txtUsername.encode("utf-8").decode("latin-1"), max_age=7 * 24 * 3600)
                    res.set_cookie("txtPassword", txtPassword, max_age=7 * 24 * 3600)
                return res
        elif txtpwd and stat:
            res = redirect("shopapp:indent")
            request.session["log"] = txtUsername
            request.session["login"] = "ok"
            if autologin:
                res.set_cookie("txtUsername",txtUsername.encode("utf-8").decode("latin-1"), max_age=7 * 24 * 3600)
                res.set_cookie("txtPassword",txtPassword,max_age=7 * 24 * 3600)
            return res
    return redirect("userapp:login")
def regist(request):
    fla=request.GET.get("flag")
    request.session["fla"]=fla
    return render(request,'userapp/register.html')
def getcaptcha(request):
    #构造一个图片验证码的对象
    image=ImageCaptcha()
    rand_code=random.sample(string.ascii_letters+string.digits,4)
    rand_code="".join(rand_code)
    request.session["code"]=rand_code
    print(rand_code,"21行")
    data=image.generate(rand_code)
    return HttpResponse(data,"image/png")

def verify_emil(request):  #验证邮箱
    code = request.GET.get("code")
    email_ok = Confirm_string.objects.filter(code=code)
    if email_ok:
        ee=email_ok[0].email
        user = TUser.objects.get(email=ee)
        user.status = 1
        user.save()
        email_ok.delete()
        return redirect("userapp:login")
    return HttpResponse("激活失败")

def send_email(txtusername,codes):
    subject='python157'
    from_email='li1301899656@sina.com'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/userapp/verify_emil?code={}"target = blank > www.baidu.com < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '.format('127.0.0.1:8000',codes)
    msg = EmailMultiAlternatives(subject, text_content,from_email, [txtusername])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
def hash_code(txtusername):
    h=hashlib.md5()
    h.update(txtusername.encode())
    return h.hexdigest()


def make_confirm_string(a):
    print(a,'188')

    codes=hash_code(a)
    Confirm_string.objects.create(code=codes,email=a)
    return codes


def registlogic(request):
    code=request.session.get("code")
    ffff=request.session.get("cars")
    txt_username=request.POST.get("txt_username")
    txt_password=request.POST.get("txt_password")
    request.session["usernum"]=txt_username
    request.session["userpas"]=txt_password
    txt_repassword=request.POST.get("txt_repassword")#确认密码
    txt_vcode=request.POST.get("txt_vcode")#验证码
    if txt_password==txt_repassword:
        txt_password = make_password(txt_password)#加密
        print(txt_password)
        if txt_username and txt_vcode and txt_password:
            result=TUser.objects.filter(email=txt_username,password=txt_password)
        else:
            return HttpResponse("不能为空")
        if result:
            return HttpResponse("账号存在")
        if txt_vcode.upper()==code.upper():
            insert=TUser.objects.create(email=txt_username,password=txt_password)
            a=TUser.objects.filter(email=txt_username)[0]
            print(a,'214邮箱')
            codes = make_confirm_string(a.email)
            send_email(txt_username, codes)
            if insert:
                request.session["re_name"]=txt_username
                request.session["re_pwd"]=txt_password
                return redirect("userapp:registok")
    return HttpResponse("注册失败")
def checkname(request):
    txt_username = request.GET.get("txt_username")
    result=TUser.objects.filter(email=txt_username)
    if result:
        return HttpResponse("1")
    elif not txt_username:
        return HttpResponse("2")
    else:
        return HttpResponse("0")
def checkImg(request):
    img=request.GET.get("txt_vcode")
    code=request.session.get("code")
    if img.upper()==code.upper():
        return HttpResponse("0")
    else:
        return HttpResponse("1")
def registok(request):
    txt_username=request.session.get("usernum")
    txt_password=request.session.get("userpas")
    return render(request,'userapp/register ok.html',{"txt_username":txt_username})