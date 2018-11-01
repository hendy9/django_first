from django.shortcuts import render
from django.http import HttpResponse
from Second_test.models import *
from . import forms
# Create your views here.

def index(request):
    webpage= AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage}
    my_dict = {'insert_me':"I am in bitch"}
    return render(request,'index.html', context=date_dict)



def form_name_view(request):
    form = forms.FormName()

    if request.method=="POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("secues")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    return render(request,'form_page.html', {'form':form})
