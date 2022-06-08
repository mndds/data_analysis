import re
from tokenize import Number
from venv import create
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseServerError

from predict.models import Prediction

from .prediction import predict_CVD

from .forms import NewForm


    # response = {'age': 7325,
    #         'gender': 2,
    #         'height': 168,
    #         'weight': 62.0,
    #         'ap_hi': 110,
    #         'ap_lo': 80,
    #         'cholesterol': 1,
    #         'gluc': 1,
    #         'smoke': 0,
    #         'alco': 0,
    #         'active': 1,
    #         'years': 20
    # }

    #Bulegenov
    # response = {'age': int(request.POST.get('age')),
    #         'gender': 2,
    #         'height': 161,
    #         'weight': 78.0,
    #         'ap_hi': 130,
    #         'ap_lo': 80,
    #         'cholesterol': 1,
    #         'gluc': 1,
    #         'smoke': 0,
    #         'alco': 0,
    #         'active': 1,
    #         'years': 72
    # }

    # response = {'age': int(request.POST.get('age')),
    #         'gender': int(request.POST.get('gender')),
    #         'height': int(request.POST.get('height')),
    #         'weight': float(request.POST.get('weight')),
    #         'ap_hi': int(request.POST.get('ap_hi')),
    #         'ap_lo': int(request.POST.get('ap_lo')),
    #         'cholesterol': int(request.POST.get('cholesterol')),
    #         'gluc': int(request.POST.get('gluc')),
    #         'smoke': bool(request.POST.get('smoke')),
    #         'alco': bool(request.POST.get('alco')),
    #         'active': bool(request.POST.get('active')),
    #         'years': int(request.POST.get('years'))
    
def main(request):
    return render(request, 'prediction/index.html', {'title': 'main page'})


def test01(request):

    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.cleaned_data.update({'age': (365*list(form.cleaned_data.values())[11])})
            prediction_result = predict_CVD(form.cleaned_data).tolist()
            context = {
                'prediction_result':prediction_result,
                'pred_nonCVD': str(round(prediction_result[0][1],3) * 100),
                'pred_CVD': str(round(prediction_result[0][0],3) * 100),
                'title':'Резльтат прогнозирования:',
                'form' : form,    
            }
            result = form.save()
            return render(request, 'prediction/test01.html', context = context)
            
            
    else:
        form = NewForm()

    return render(request, 'prediction/test01.html', {'form' : form, 'title':'Введите ваши данные: '})

def calculate(request):

    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():            
            form.cleaned_data.update({'age': (365*list(form.cleaned_data.values())[12])})
            print(form.cleaned_data)
            print('AGE : ', (365 * list(form.cleaned_data.values())[12])) 
            
            prediction_result = predict_CVD(form.cleaned_data).tolist()
            context = {
                'prediction_result':prediction_result,
                'pred_nonCVD': str(round(prediction_result[0][0],3) * 100),
                'pred_CVD': str(round(prediction_result[0][1],3) * 100),
                'title':'Результат прогнозирования:',
                'form' : form,    
            }
            
            form.cleaned_data.update({'cvd': (round(prediction_result[0][1],3) * 100)})
            form.cleaned_data.update({'cvd_non': (round(prediction_result[0][0],3) * 100)})
            Prediction.objects.create(**form.cleaned_data)
            #result = form.save()
            
            return render(request, 'prediction/calculate.html', context = context)            
    else:
        form = NewForm()

    return render(request, 'prediction/calculate.html', {'form' : form, 'title':'Введите ваши данные: '})

