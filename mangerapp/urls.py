from django.urls import path

from mangerapp import views

app_name="main"
urlpatterns = [
    path('index/', views.index,name="index"),
    path('add/', views.add,name="add"),
    path('addlogic/', views.addlogic,name="addlogic"),
    path('dzlist/', views.dzlist,name="dzlist"),
    path('list/', views.list,name="list"),
    path('splb/', views.splb,name="splb"),
    path('test/', views.test,name="test"),
    path('zjsp/', views.zjsp,name="zjsp"),
    path('zjzlb/', views.zjzlb,name="zjzlb"),
]