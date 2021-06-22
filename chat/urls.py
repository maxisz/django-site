from django.urls import path
from . import views

urlpatterns = [
    path('deletechat/<int:room>',views.delete_chat, name='deletechat'),
    path('home/', views.home, name='home'),
    path('joinroom/', views.joinroom , name='joinroom'),
    path('', views.home, name='home'),
    path('joinroom/checkview', views.checkview, name='checkview'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]