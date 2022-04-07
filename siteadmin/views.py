from django.shortcuts import render,redirect
from django.http import HttpResponse
from poolhost import *
from poolhost.models import vehicle_register, VehicleType
from accounts.models import User
from accounts.forms import *
from .forms import UserRegisterForm

# def index(request)
#     return render(request, template_name)

def index(request):
    return render(request, 'siteadmin/index.html')

def createsiteadmin(request):
    if request.method == 'POST':
        form = SiteAdminForm(request.POST,request.FILES)

        if form.is_valid(siteadmin=True):
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect("site_admin")
        else:
            print(form.errors)
            return HttpResponse("Error")
    else:
        form = SiteAdminForm()
    return render(request, 'Create_admin.html', {'form': form})

def admin_list(request):
    data = User.objects.filter(is_superadmin=True)
    return render(request, 'siteadmin/admin_list.html',{'data':data})

    
def siteadmin_update(request, id):
    instance = admin_register.objects.get(id=id)
    form = SiteAdminForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect("admin_list")
    else:
        print(form.errors)
        return render(request, 'create_admin.html', {'form': form, 'instance': instance})


def delete_admin(request, id):
    if user .is_siteadmin(True):
        admin_register.objects.get(id=id).delete()
        return redirect("admin_list")



def create_host(request):
    if request.method == 'POST':
        form = VehicleRegisterForm(request.POST, request.FILES)

        if form.is_valid(poolhost=True):
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect("host_list")
        else:
            print(form.errors)
            return HttpResponse("Error")
    else:
        form = VehicleRegisterForm()
    return render(request, 'create_host.html', {'form': form})


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
    if user .is_host(True):
        vehicle_register.objects.get(id=id).delete()
        return redirect("host_list")


def create_user(request):
    if request.method == 'POST':
        form = PoolUserForm(request.POST, request.FILES)

        if form.is_valid(pooluser=True):
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect("user_list")
        else:
            print(form.errors)
            return HttpResponse("Error")
    else:
        form = PoolUserForm()
        return render(request, 'create_user.html', {'form': form})


def user_list(request):
    data = user_register.objects.all()
    return render(request, 'user_list.html', {'data': data})    

def pooluser_update(request, id):
    instance = user_register.objects.get(id=id)
    form = PoolUserForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect("user_list")
    else:
        print(form.errors)
    return render(request, 'create_user.html', {'form': form, 'instance': instance})    


def delete_user(request, id):
    user_register.objects.get(id=id).delete()
    return redirect("user_list")



def create_siteadmin(request):
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_superadmin = True
            user.set_password(request.POST.get('password'))
            user.save()

            return redirect('siteadmin:index')
        else:
            print(forms.errors)
            return redirect('siteadmin:index')
    else:
        form = UserRegisterForm()
        return render(request, 'siteadmin/create_siteadmin.html', {'form': form})


def create_poolhost(request):
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_poolhost = True
            user.set_password(request.POST.get('password'))
            user.save()

            return redirect('siteadmin:index')
        else:
            print(forms.errors)
            return redirect('siteadmin:index')
    else:
        form = UserRegisterForm()
        return render(request, 'siteadmin/create_poolhost.html', {'form': form})