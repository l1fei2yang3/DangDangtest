from django.urls import path

from mangerapp import views

app_name="main"
urlpatterns = [
    path('index/', views.index,name="index"),
    path('login/', views.login,name="login"),
    path('loginlogic/', views.loginlogic,name="loginlogic"),
    path('add/', views.add,name="add"),
    path('addlogic/', views.addlogic,name="addlogic"),
    path('delete/', views.delete,name="delete"),
    path('update_book/', views.update_book,name="update_book"),
    path('update_booklogic/', views.update_booklogic,name="update_booklogic"),
    path('dzlist/', views.dzlist,name="dzlist"),
    path('list/', views.list,name="list"),
    path('splb/', views.splb,name="splb"),
    path('delete_category/', views.delete_category,name="delete_category"),
    path('delete_all/', views.delete_all,name="delete_all"),
    path('test/', views.test,name="test"),
    path('zjsp/', views.zjsp,name="zjsp"),
    path('zjsplogic/', views.zjsplogic,name="zjsplogic"),
    path('zjzlb/', views.zjzlb,name="zjzlb"),
    path('zjzlblogic/', views.zjzlblogic,name="zjzlblogic"),
]