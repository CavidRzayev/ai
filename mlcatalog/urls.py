
from django.urls import path,include
from .views import *

urlpatterns = [
    path("catalog/",catalog,name="mlcatalog")
]