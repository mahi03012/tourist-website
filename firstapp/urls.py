from django.urls import path

from . import views

urlpatterns = [
		path('',views.index, name='index'),
		path('Home',views.Home, name='Home'),
		path('News',views.News,name='News'),
		path('contact',views.contact,name='contact')
        
	]
