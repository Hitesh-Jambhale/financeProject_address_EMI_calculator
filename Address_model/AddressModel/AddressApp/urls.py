from django.urls import path
from . import views

urlpatterns =[
    path('Address/',views.AddAddress,name='Address'),
    path('showAddress/',views.ShowAddress,name='show'),
    path('update/<int:i>/',views.updateAddress,name='update'),
    path('delete/<int:i>/',views.deleteAddress,name='delete')

]