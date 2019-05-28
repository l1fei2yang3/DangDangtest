from django.urls import path,include

from indexapp import views

app_name='indexapp'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('booklist/',views.booklist,name='booklist'),
    path('bookdetails/',views.bookdetails,name='bookdetails'),
]
