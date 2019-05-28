from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from userapp.models import TUser, TCategory, TBook


def index(request):
    exit = request.GET.get("exit")
    request.session["exit"]="1"
    stauts=request.session.get("login")
    user=request.session.get("log")
    new_books=TBook.objects.all().order_by("pushish_time","book_name")[:8]#新书上架
    sales_book=TBook.objects.all().order_by("sales","book_name")[:5]#热卖榜
    saless_book=TBook.objects.all().order_by("sales","book_name")[:10]#热卖榜
    flag=request.GET.get("flag")
    first_cate=TCategory.objects.filter(parent_id=0)
    second_cate=TCategory.objects.filter(parent_id__gt=0)
    if flag is None or flag=="index":
        flag="index"
    print(exit,'11行')
    if exit:
        del request.session["login"]
        stauts=request.session.get("login")
    print(stauts,'10行')
    if stauts and user:
        # username=TUser.objects.filter(email=user)[0].username
        username=user[0:3]+"***"+user[-4:]
        print(username)
    else:
        username=None
        print(username,'22行')
    return render(request,'indexapp/index.html',{"username":username,"flag":flag,"first_cate":first_cate,"second_cate":second_cate,"new_books":new_books,"sales_book":sales_book,"saless_book":saless_book})

def booklist(request):
    number=request.GET.get("number")
    print(number,'36行')
    if not number:
        number=1
    stauts = request.session.get("login")
    user = request.session.get("log")
    exit = request.GET.get("exit")
    cate_id=request.GET.get("cate_id")
    bookli=TBook.objects.filter(category_id=cate_id)
    first_cate = TCategory.objects.filter(parent_id=0)
    second_cate = TCategory.objects.filter(parent_id__gt=0)
    print(bookli.count(),"44行")
    pagtor = Paginator(bookli,per_page=3)
    print(pagtor,"48行")
    page = pagtor.page(number)
    print(page,"50行")
    if exit:
        del request.session["login"]
        stauts = request.session.get("login")
    if stauts and user:
        username = user[0:3] + "***" + user[-4:]
    else:
        username = None
    return render(request,'indexapp/booklist.html',{"number":number,"page":page,"bookli":bookli,"username":username,"first_cate":first_cate,"second_cate":second_cate,"cate_id":cate_id})

def bookdetails(request):
    book_id=request.GET.get("book_id")
    stauts = request.session.get("login")
    user = request.session.get("log")
    exit = request.GET.get("exit")
    book_details=TBook.objects.filter(id=book_id)
    if exit:
        del request.session["login"]
        stauts=request.session.get("login")
    if stauts and user:
        username = user[0:3] + "***" + user[-4:]
    else:
        username = None
    return render(request,'indexapp/Book details.html',{"username":username,"book_details":book_details})