from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def fanlar(request):
    if request.method == "POST":
        Fan.objects.create(
        nom = request.POST.get('nom'),
        yonalish = Yonalish.objects.get(id=request.POST.get('yonalish')),
        asosiy = request.POST.get('asosiy')
        )
        return redirect('/fan/')
    fan = Fan.objects.all()
    yonalishlar = Yonalish.objects.all()
    context = {
        'fan': fan,
        'yonalish': yonalishlar
    }
    return render(request, 'Fan.html', context)
