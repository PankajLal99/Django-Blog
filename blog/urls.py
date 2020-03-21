from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('post/<str:pk>/',views.show,name='show'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('signup/',views.signup,name='signup'),
]
