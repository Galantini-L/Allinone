from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('number',views.number,name='number'),

]


"""
1era parte del tutorial hecha, seguir desde el principio de
la 2da parte. :D
"""