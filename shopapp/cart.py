#购物车队列类
from userapp.models import TBook


class CartItem():
    def __init__(self,book,amount):
        self.amount=amount
        self.book=book
        #删除状态
        self.status=1
class Cart():
    def __init__(self):
        self.save_price=0 #节省钱
        self.total_price=0 #总钱
        self.cartItem=[] #购物车队列

    #计算购物车中商品的节省金额以及总金额
    def sums(self):
        self.total_price=0
        self.save_price=0
        for i in self.cartItem:
            self.total_price+=i.book.dangdang_price*int(i.amount)
            self.save_price+=(i.book.market_price-i.book.dangdang_price)*int(i.amount)
    #向购物车中添加书籍
    def add_book_toCart(self,bookid):
        book = TBook.objects.filter(id=bookid)[0]
        print(bookid,type(bookid),'26行')
        for i in self.cartItem:
            if i.book.id==book.id:
                print("29行")
                i.amount+=1
                self.sums()
                return
        self.cartItem.append(CartItem(book,1))
        self.sums()
    #修改购物车的商品信息
    def modify_cart(self,bookid,amount):
        print(bookid,amount,'38行')
        for i in self.cartItem:
            if i.book.id==int(bookid):
                i.amount=amount
        self.sums()
    #删除购物车
    def delete_book(self,bookid):
        for i in self.cartItem:
            if i.book.id==int(bookid):
                self.cartItem.remove(i)
        self.sums()

