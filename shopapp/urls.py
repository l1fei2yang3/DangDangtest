from django.urls import path,include

from shopapp import views

app_name='shopapp'
urlpatterns = [
    path('car/',views.car,name='car'),
    path('add_book/',views.add_book,name='add_book'),
    path('update_cart/',views.update_cart,name='update_cart'),
    path('delete_book_inCart/',views.delete_book_inCart,name='delete_book_inCart'),
    path('indent/',views.indent,name='indent'),
    path('order/',views.order,name='order'),
    path('indentok/',views.indentok,name='indentok'),
]
