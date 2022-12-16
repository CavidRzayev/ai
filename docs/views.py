from django.shortcuts import render
from docs.models import *
from src.models import Category,SubCategory


def docs(request):
    docs = Doc.objects.get(id=1)
    category = Category.objects.all()
    context = {
        "data":docs,
        "category":category
    }
    return render(request,"docs.html",context)


def detail_subcategory(request,id):
    data = SubCategory.objects.get(id=id)
    category = Category.objects.all()
    context = {
        "data":data,
        "category":category
    }

    return render(request,"detail.html",context)