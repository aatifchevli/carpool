from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.


def index(request):
     return render(request, 'poolhost/index.html')


def vehicle_register(request):
    if request.method == 'POST':
        form = VehicleRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect("poolhost:index")
        else:
            print(form.errors)
            return HttpResponse("Error")
    else:
        form = VehicleRegisterForm()
    return render(request, 'poolhost/vehicle_register.html', {'form': form})


def host_list(request):
    # data = vehicle_register.objects.get(id=1)
    # data = vehicle_register.objects.filter(name__contains="demo1")
    data = vehicle_register.objects.all()
    return render(request, 'host_list.html', {'data': data})


def poolhost_update(request, id):
    instance = vehicle_register.objects.get(id=id)
    form = VehicleRegisterForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect("host_list")
    else:
        print(form.errors)
    return render(request, 'create_host.html', {'form': form, 'instance': instance})


def delete_host(request, id):
    vehicle_register.objects.get(id=id).delete()
    return redirect("host_list")

def VehicleType(request):
    if request.method == 'POST':
        form = Vehicle_Type(request.POST, request.FILES)

        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect("poolhost:index")
        else:
            print(form.errors)
            return HttpResponse("Error")
    else:
        form = Vehicle_Type()
    return render(request, 'poolhost/vehicletype.html', {'form': form})


def vehicletype_update(request, id):
    instance = VehicleType.objects.get(id=id)
    form = VehicleType(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect("vehicle_list")
    else:
        print(form.errors)
    return render(request, 'vehicle_register.html', {'form': form, 'instance': instance})


def delete_vehicletype(request, id):
    vehicle_register.objects.get(id=id).delete()
    return redirect("vehicle_list")