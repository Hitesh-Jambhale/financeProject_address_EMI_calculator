from django.shortcuts import render

# Create your views here.

def simpleView(request):
    template_name = 'emi_cal/emi.html'
    context = {}
    return render(request, template_name, context)