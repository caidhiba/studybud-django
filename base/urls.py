from django.urls import path

from . import views

urlpatterns = [

     # the line below this comment means when the user click this url call the functio home
   
    # means in the file path if i add /room i will get the function so(urls)triggers views and tats what the user 
    # will see
 
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
]