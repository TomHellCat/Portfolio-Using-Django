from .import views
from django.urls import path

app_name = 'base'

urlpatterns = [
	path('', views.index, name='index'),
	path('about',views.aboutme, name='aboutme'),
	path('get_name',views.get_name, name='get_name'),
]