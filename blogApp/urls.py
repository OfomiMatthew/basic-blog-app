from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('post',views.post,name='post'),
    path('details/<int:id>/',views.details,name="details"),
    # path('create',views.create, name='create')
    
]
