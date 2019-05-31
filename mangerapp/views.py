from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
import os
import uuid

from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from userapp.models import TBook


def index(request):
    return render(request,'index.html')
def add(request):#添加表
    return render(request,'main/add.html')
def addlogic(request):#添加书本逻辑，接收表单中的值
    productname=request.POST.get("productname")#商品名称
    author=request.POST.get("author")#作者
    press=request.POST.get("press")#出版社
    publication_time=request.POST.get("publication_time")#出版时间
    market_price=request.POST.get("market_price")#原价/市场价
    dangdang_price=request.POST.get("dangdang_price")#当当价
    pics=request.FILES.get("book_price")#书籍图片
    if productname and author and press and publication_time and market_price and dangdang_price: #判断值是否为空
        ext=os.path.splitext(pics.name)[1]#切割出文件的后缀名
        pics.name=str(uuid.uuid4())+ext #随机生成文件名并拼接上切割出来的原文件的后缀名
        #向数据库的book表插入数据
        insert=TBook.objects.create(book_name=productname,anthor=author,book_publish=press,pushish_time=publication_time,market_price=market_price,dangdang_price=dangdang_price,pics=pics)
        #如果插入成功
        if insert:
            #返回提示信息
            return HttpResponse("提交成功")
        return HttpResponse("提交失败")
    return HttpResponse("不能为空")
def dzlist(request):
    return render(request,'main/dzlist.html')
def list(request):#商品列表
    number = request.GET.get("number")#获取前端传来的页码
    if not number: #判断如果页面为空的话
        number=1 #页码的值默认为1
    select=TBook.objects.all()#查询全部书籍
    pagtor = Paginator(select, per_page=6)#将查询到的数据进行每一页6条数据划分
    page = pagtor.page(number)#统计出划分出来的页码值
    # 渲染页面并将查询到全部书籍的QuerySet对象发送到前端页面
    return render(request,'main/list.html',{"select":select,"page":page})
def splb(request):
    return render(request,'main/splb.html')
def test(request):
    return render(request,'main/test.html')
def zjsp(request):
    return render(request,'main/zjsp.html')
def zjzlb(request):
    return render(request,'main/zjzlb.html')