from datetime import datetime
import time

from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from shopapp.cart import Cart
from userapp.models import TAddress, TUser, TOrder


def car(request):
    cart=request.session.get("cart")
    stauts = request.session.get("login")
    user = request.session.get("log")
    print(user,cart,'16行的car')
    exit = request.GET.get("exit")
    print(stauts,user,'17行stauts')
    if exit:
        del request.session["login"]
        stauts=request.session.get("login")
    if stauts and user:
        username = user[0:3] + "***" + user[-4:]
    else:
        username = None
    if cart is None:
        return render(request,'shopapp/car.html',{"username":username,"cartItem":cart,"s_price":0,"t_price":0})
    else:
        length = len(cart.cartItem)
        request.session["cartItem"]=cart.cartItem
        request.session["s_price"]=cart.save_price
        request.session["t_price"]=cart.total_price
        print(username,'32行username')
        return render(request,'shopapp/car.html',{"username":username,"cartItem":cart.cartItem,"s_price":cart.save_price,"t_price":cart.total_price,"length":length})

def add_book(request):
    #接收参数
    bookid=request.GET.get("bookid")
    amount=request.GET.get("amount")
    print(bookid,amount,'20行')
    cart=request.session.get("cart")
    print(cart,"32行")
    #判断购物车是否存在
    if cart is None:
        cart=Cart()
        cart.add_book_toCart(bookid)
        #将购物车存入session中
        request.session["cart"]=cart
    else:
        cart.add_book_toCart(bookid)
        #将购物车存入session中
        request.session["cart"]=cart
    #将数据响应到模板
    if bookid and amount:
        return HttpResponse("ok")
    # return HttpResponse("no")

def update_cart(request):
    bookid=request.GET.get("bookid")
    amount=request.GET.get("amount")
    print(bookid,amount,'52行')
    cart=request.session.get("cart")
    cart.modify_cart(bookid,amount)
    request.session["cart"]=cart
    total_price=cart.total_price
    save_price=cart.save_price
    return JsonResponse ({"total_price":total_price,"save_price":save_price})
def delete_book_inCart(request):
    bookid=request.GET.get("bookid")
    cart=request.session.get("cart")
    cart.delete_book(bookid)
    request.session["cart"]=cart
    total_price = cart.total_price
    save_price = cart.save_price
    length=len(cart.cartItem)
    request.session["length"]=length
    return JsonResponse ({"total_price":total_price,"save_price":save_price,"length":length})
def indent(request):
    cart=request.GET.get("flag")
    stat=request.GET.get("stat")
    if stat:
        request.session["stat"]=stat
    num=request.GET.get("num")
    print(stat,"76行")
    stauts = request.session.get("login")
    user = request.session.get("log")
    exit = request.GET.get("exit")
    # cartItem=request.session["cartItem"]
    cartItem=request.session.get("cartItem")
    if cartItem is None:
        return redirect("shopapp:car")
    s_price=request.session.get("s_price")
    t_price=request.session.get("t_price")
    print(cart,'75行cart')
    useremail = request.session.get("log")
    # if cart is None:
    #     request.session["jiesuan"]="1"
    #     print('indentview的101行')
    #     return redirect("userapp:login")
    # else:
    if exit:
        del request.session["login"]
        stauts = request.session.get("login")
    if stauts and user:
        username = user[0:3] + "***" + user[-4:]
    else:
        username = None
    if useremail:
        userid = TUser.objects.filter(email=useremail)[0].id
        addr = TAddress.objects.filter(user_id=userid)
        return render(request,'shopapp/indent.html',{"username":username,"cartItem":cartItem,"s_price":s_price,"t_price":t_price,"addr":addr})
    else:
        request.session["jiesuan"] = "1"
        print('indentview的101行')
        return redirect("userapp:login")
def order(request):
    name = request.GET.get("ship_man")
    request.session["name"]=name
    address = request.GET.get("ship_address")
    zip = request.GET.get("ship_zip")
    phone = request.GET.get("ship_phone")
    countmoney = request.GET.get("countmoney")
    useremail=request.session.get("log")
    print(name,type(name),address,type(address),zip,type(zip),phone,type(phone),useremail,type(useremail), '100行')
    userid=TUser.objects.filter(email=useremail)[0].id
    print(userid,type(userid),'104行')
    orderid=int(time.time()*1000)+int(time.clock()*1000000)
    request.session["orderid"]=orderid
    print(orderid,type(orderid),'112行')
    TOrder.objects.create(order_price=countmoney,create_time=str(datetime.now()),order_id=orderid,user_id=userid,receive_address=address)
    select=TAddress.objects.filter(recever=name,receve_address=address,zip_code=zip,phone=phone,user_id=userid)
    if not select:
        TAddress.objects.create(recever=name,receve_address=address,zip_code=zip,phone=phone,user_id=userid)
        if name and address and zip and phone:
            return HttpResponse("1")
    else:
        return  HttpResponse("1")
def indentok(request):
    orderid=request.session.get("orderid")
    t_price = request.session["t_price"]
    cartItem = request.session["cartItem"]
    i=0
    for c in cartItem:
        i+=1
    name = request.session["name"]
    stauts = request.session.get("login")
    user = request.session.get("log")
    exit = request.GET.get("exit")
    if exit:
        del request.session["login"]
        stauts = request.session.get("login")
    if stauts and user:
        username = user[0:3] + "***" + user[-4:]
    else:
        username = None
    return render(request,'shopapp/indent ok.html',{"username":username,"orderid":orderid,"t_price":t_price,"name":name,"i":i})