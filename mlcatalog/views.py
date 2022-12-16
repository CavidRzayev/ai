from django.shortcuts import render
import pandas as pd


def catalog(request):
    data = pd.read_excel("Modelling_Catalog_Combined_v4.xlsx")
    print(data)
    context = {
        "df":data
    }
    return render(request,"catalog.html",context)
