from django.urls import path
from . import views

app_name= 'my_app'

urlpatterns =[
    path('', views.examply_view, name='example'),
    path('variable/', views.variable,name='variable')
]