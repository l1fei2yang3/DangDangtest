from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
import os
import uuid

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from userapp.models import TBook, TAddress, TCategory


def index(request):
    stat=request.session.get("lo")#获取登录状态
    if stat:
        return render(request, 'index.html')
    return redirect('main:login')
def login(request):
    return render(request,'main/login.html')
def loginlogic(request):
    name=request.POST.get("name")#获取用户名
    pwd=request.POST.get("pwd")#获取密码
    if name=='123456' and pwd=='123456':
        request.session["lo"] = "ok"
        return redirect('main:index')
def add(request):  # 添加表
    categoty = TCategory.objects.filter(parent_id__gt=0)  # 查询所有二级类别
    return render(request, 'main/add.html', {'categoty': categoty})


def addlogic(request):  # 添加书本逻辑，接收表单中的值
    productname = request.POST.get("productname")  # 商品名称
    author = request.POST.get("author")  # 作者
    press = request.POST.get("press")  # 出版社
    categoty = request.POST.get("categoty")  # 商品类别
    categoty_id = TCategory.objects.filter(category_name=categoty)[0].id  # 通过商品类别名查询到对应的商品类别id
    publication_time = request.POST.get("publication_time")  # 出版时间
    market_price = request.POST.get("market_price")  # 原价/市场价
    dangdang_price = request.POST.get("dangdang_price")  # 当当价
    pics = request.FILES.get("book_price")  # 书籍图片
    if productname and author and press and publication_time and market_price and dangdang_price:  # 判断值是否为空
        ext = os.path.splitext(pics.name)[1]  # 切割出文件的后缀名
        pics.name = str(uuid.uuid4()) + ext  # 随机生成文件名并拼接上切割出来的原文件的后缀名
        # 向数据库的book表插入数据
        insert = TBook.objects.create(book_name=productname, anthor=author, book_publish=press, category_id=categoty_id,
                                      pushish_time=publication_time, market_price=market_price,
                                      dangdang_price=dangdang_price, pics=pics)
        # 如果插入成功
        if insert:
            # 返回提示信息
            return HttpResponse("提交成功")
        return HttpResponse("提交失败")
    return HttpResponse("不能为空")


def dzlist(request):  # 地址列表
    number = request.GET.get("number")  # 获取前端传来的页码
    if not number:  # 判断如果页面为空的话
        number = 1  # 页码的值默认为1
    select = TAddress.objects.all()  # 查询全部地址信息
    pagtor = Paginator(select, per_page=6)  # 将查询到的数据进行每一页6条数据划分
    page = pagtor.page(number)  # 统计出划分出来的页码值
    # 渲染页面并将查询到全部书籍的QuerySet对象发送到前端页面
    return render(request, 'main/dzlist.html', {'select': select, "page": page, 'number': number})


def list(request):  # 商品列表
    number = request.GET.get("number")  # 获取前端传来的页码
    if not number:  # 判断如果页面为空的话
        number = 1  # 页码的值默认为1
    select = TBook.objects.filter(category__parent_id__gt=0).values('category__category_name', 'id', 'book_name',
                                                                    'storage', 'anthor', 'book_publish', 'market_price',
                                                                    'dangdang_price', 'pics')  # 查询全部书籍
    pagtor = Paginator(select, per_page=6)  # 将查询到的数据进行每一页6条数据划分
    num = request.session.get("dele_number")#获取到删除页码
    if not num:  # 判断接收到的共享的页码值是否为空
        page = pagtor.page(number)  # 如果是空值，就将前端接收到的页码值给page
    else:
        del request.session["dele_number"]  # 否则的话就删除掉共享的页码
        # num=int(select.count() / 6)+1 #如果不是最后一页的话，在删除掉6个数据后还定位在当前页
        # print(num,'63行')
        page = pagtor.page(num)  # 统计出划分出来的页码值
    # 渲染页面并将查询到全部书籍的QuerySet对象发送到前端页面
    return render(request, 'main/list.html', {"select": select, "page": page, 'number': number, })


def delete(request):
    id = request.GET.get("id")  # 接收前端发来的商品id
    number = request.GET.get("number")  # 接收前端发来的页面所在的页码
    cout = TBook.objects.all().count()  # 查询数据库中所有书籍并且计数
    if cout % 6 == 1 and int(number) > 1:  # 判断书籍总数量是否能够整除6(因为一个页面显示6条数据)并且返回的页码值是否大于1
        number = int(number) - 1  # 满足条件页码就减1
    de_id = TBook.objects.filter(id=id)[0]  # 通过传来要删除的id查询对应的商品(因为查询到的是QuerySet对象，是一个list，所以通过下标0获取值)
    TBook.objects.get(id=de_id.id).delete()  # 通过商品的id删除掉对应的商品数据
    request.session["dele_number"] = number  # 将改变后的页码值共享出去
    return redirect("main:list")


def update_book(request):  # 修改商品
    id = request.GET.get("id")  # 接收前端发来的商品id
    number = request.GET.get("number")  # 接收前端发来的页面所在的页码
    up = TBook.objects.filter(id=id)[0]
    categoty = TCategory.objects.filter(parent_id__gt=0)  # 查询所有二级类别
    return render(request, 'main/update_book.html', {'categoty': categoty, 'up': up,'number':number})


def update_booklogic(request):
    id = request.GET.get("id")  # 接收前端发来的商品id
    number = request.GET.get("number")  # 接收前端发来的页面所在的页码
    productname = request.POST.get("productname")  # 商品名称
    author = request.POST.get("author")  # 作者
    press = request.POST.get("press")  # 出版社
    categoty = request.POST.get("categoty")  # 商品类别
    categoty_id = TCategory.objects.filter(category_name=categoty)[0].id  # 通过商品类别名查询到对应的商品类别id
    market_price = request.POST.get("market_price")  # 原价/市场价
    dangdang_price = request.POST.get("dangdang_price")  # 当当价
    storage = request.POST.get("storage")  # 库存
    pics = request.FILES.get("book_price")  # 书籍图片
    update = TBook.objects.filter(id=id)[0]#按照id查询对应的书籍
    if pics:#如果图片有值
        ext = os.path.splitext(pics.name)[1]  # 切割出文件的后缀名
        pics.name = str(uuid.uuid4()) + ext  # 随机生成文件名并拼接上切割出来的原文件的后缀名
        update.pics = pics
    # 向数据库的book表修改数据
    update.book_name = productname
    update.anthor = author
    update.book_publish = press
    update.category_id = categoty_id
    update.market_price = market_price
    update.dangdang_price = dangdang_price
    update.storage = storage
    update.save()#更新保存
    request.session["upnumber"] = number#共享更新页码
    # 返回提示信息
    return redirect('main:list')


def splb(request):
    number = request.GET.get("number")  # 获取前端传来的页码
    if not number:  # 判断如果页面为空的话
        number = 1  # 页码的值默认为1
    # 查询到类别表中父类id大于0的数据和对应书籍的书名
    num = request.session.get("dlcate_number")
    book_select = TBook.objects.filter(category__parent_id__gt=0).values("category__category_name", "book_name")
    pagtor = Paginator(book_select, per_page=6)  # 将查询到的数据进行每一页6条数据划分
    if not num:  # 判断接收到的共享的页码值是否为空
        page = pagtor.page(number)  # 如果是空值，就将前端接收到的页码值给page
    else:
        del request.session["dlcate_number"]  # 否则的话就删除掉共享的页码
        page = pagtor.page(num)  # 统计出划分出来的页码值
    return render(request, 'main/splb.html', {'book_select': book_select, "page": page, 'number': number})


def delete_category(request):
    category_name = request.GET.get("category_name")  # 接收前端发来的类别名
    number = request.GET.get("number")  # 接收前端发来的页面所在的页码
    cout = TCategory.objects.filter(parent_id__gt=0).count()  # 查询数据库中所有书籍并且计数
    if cout % 6 == 1 and int(number) > 1:  # 判断书籍总数量是否能够整除6(因为一个页面显示6条数据)并且返回的页码值是否大于1
        number = int(number) - 1  # 满足条件页码就减1
    TCategory.objects.get(category_name=category_name).delete()  # 通过类别名删除对应的数据
    request.session["dlcate_number"] = number  # 将改变后的页码值共享出去
    return redirect("main:splb")


def test(request):
    return render(request, 'main/test.html')


def zjsp(request):
    return render(request, 'main/zjsp.html')
def zjsplogic(request):
    father=request.GET.get("father")#接收父类数据
    TCategory.objects.create(category_name=father,parent_id=0)
    return  HttpResponse("添加成功")

def zjzlb(request):
    categoty = TCategory.objects.filter(parent_id__lt=1)  # 查询所有一级类别
    return render(request, 'main/zjzlb.html',{'categoty':categoty})
def zjzlblogic(request):
    category_child=request.GET.get('category_child')#接收二级分类
    category=request.GET.get('category')#接收一级分类
    c_id=TCategory.objects.filter(category_name=category)[0].id
    TCategory.objects.create(category_name=category_child,parent_id=c_id)
    return HttpResponse("添加成功")
def delete_all(request):
    id=request.GET.get("id")
    id=id.split(",")
    for i in range(len(id)):
        TBook.objects.get(id=int(id[i])).delete()
    return redirect('main:index')
