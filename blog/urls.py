from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('post/<str:pk>/',views.show,name='show'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('userpost/',views.proindex,name='userpost'),
    path('crud/<str:pk>/',views.crud,name='crud'),
    path('delete/<str:pk>/',views.deletepost,name='delete'),
]
