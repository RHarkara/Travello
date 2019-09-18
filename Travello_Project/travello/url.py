from django.urls import path

from  .  import views

urlpatterns = [

    path('', views.index, name='index'),
    path('warangal.html',views.warangal, name='warangal')
    


]