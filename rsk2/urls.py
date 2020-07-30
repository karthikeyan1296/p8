from django.urls import path
from rsk2  import views
app_name="rsk2"

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('fact/<n>',views.fact,name="fact"),
    path('child',views.child,name="child"),
    path('base',views.base,name="base"),
   
]