from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PermanentAddress,CurrentAddress
from .forms import PermanentAddressForm,CurrentAddressForm

# Create your views here.

def AddAddress(request):
    form = PermanentAddressForm()
    form_1 = CurrentAddressForm()
    if request.method == 'POST':
        form = PermanentAddressForm(request.POST)
        form_1 = CurrentAddressForm(request.POST)
        if form.is_valid() and form_1.is_valid():
            form.save()
            form_1.save()
            return redirect('show')
            #return HttpResponse ('Address saved in db ')
    template_name = 'AddressApp/addAddress.html'
    context = {'form':form,'form_1':form_1}
    return render(request, template_name, context)


def ShowAddress(request):
    paddr = PermanentAddress.objects.all()
    caddr = CurrentAddress.objects.all()
    template_name = 'AddressApp/showAddress.html'
    context = {'paddr': paddr, 'caddr':caddr}
    return render(request, template_name, context)


def updateAddress(request,i):
    paddr = PermanentAddress.objects.get(id=i)
    form = PermanentAddressForm(instance=paddr)
    caddr = CurrentAddress.objects.get(id=i)
    form_1 = CurrentAddressForm(instance=caddr)
    if request.method == 'POST':
        form = PermanentAddressForm(request.POST, instance=paddr)
        form_1 = CurrentAddressForm(request.POST,instance=caddr)
        if form.is_valid() and form_1.is_valid() :
            form.save()
            form_1.save()
            return redirect('show')
    template_name = 'AddressApp/addAddress.html'
    context = {'form': form,'form_1':form_1}
    return render(request, template_name, context)


def deleteAddress(request,i):
    paddr = PermanentAddress.objects.get(id=i)
    caddr = CurrentAddress.objects.get(id=i)
    if request.method == 'POST':
        paddr.delete()
        caddr.delete()
        return redirect('show')
    template_name = 'FirstApp/deleteAddress.html'
    context = {'paddr': paddr,'caddr':caddr}
    return render(request, template_name, context)