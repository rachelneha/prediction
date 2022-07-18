from django.shortcuts import render
import numpy as np
import pickle


def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request,"predict.html")


def result(request):

    model = pickle.load(open('salemodel.pkl', 'rb'))
    var1 = int(request.GET['year'])
    pred = model.predict(np.array([var1]).reshape(1, -1))
    pred = round(pred[0])

    price = f"sale prediction on : {var1} is   "+str(pred)
    return render(request, "predict.html" , {'result2':price})