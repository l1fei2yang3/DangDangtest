from django.urls import path,include

from userapp import views
app_name='userapp'
urlpatterns = [
    path('login/',views.login,name='login' ),
    path('verify_emil/',views.verify_emil,name='verify_emil' ),
    path('loginjump/',views.loginjump,name='loginjump' ),
    path('loginlogic/',views.loginlogic,name='loginlogic' ),
    path('regist/',views.regist,name='regist' ),
    path('getcaptcha/',views.getcaptcha,name='getcaptcha' ),
    path('registlogic/',views.registlogic,name='registlogic' ),
    path('checkname/',views.checkname,name='checkname' ),
    path('checkImg/',views.checkImg,name='checkImg' ),
    path('registok/',views.registok,name='registok' ),
]