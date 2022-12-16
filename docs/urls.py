
from django.urls import path,include
from .views import *

urlpatterns = [
    path('docs/',docs,name="docs"),
    path('detail/<id>/',detail_subcategory,name="detail_subcategory"),
    
]