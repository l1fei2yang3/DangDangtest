from datetime import datetime
from django.test import TestCase
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DangDang.settings")
django.setup()
from userapp.models import TCategory, TBook
# Create your tests here.
# b55 = TBook.objects.create(book_name='第十三本教育分类下的教材图书',dangdang_price=107.00,market_price=121.00,pushish_time=datetime.now(),sales=121,storage=100,category_id=None,anthor='马云',pics="book_price/dd1.jpg")
# b56 = TBook.objects.create(book_name='第十四本教育分类下的教材图书',dangdang_price=102.00,market_price=122.00,pushish_time=datetime.now(),sales=123,storage=100,category_id=None,anthor='刘慈欣',pics="book_price/dd6.jpg")
# b57 = TBook.objects.create(book_name='第十五本教育分类下的教材图书',dangdang_price=103.00,market_price=176.00,pushish_time=datetime.now(),sales=1002,storage=100,category_id=None,anthor='刘慈欣',pics="book_price/dd3.jpg")
# b58 = TBook.objects.create(book_name='第十六本教育分类下的教材图书',dangdang_price=106.00,market_price=151.00,pushish_time=datetime.now(),sales=1040,storage=100,category_id=None,anthor='马云',pics="book_price/dd6.jpg")
# b59 = TBook.objects.create(book_name='第十一本教育分类下的教材图书',dangdang_price=123.00,market_price=641.00,pushish_time=datetime.now(),sales=10210,storage=100,category_id=None,anthor='刘慈欣',pics="book_price/dd5.jpg")
#
