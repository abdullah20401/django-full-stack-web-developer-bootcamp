from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request, 'TestApp/index.html', context=date_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")

            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])
    
    return render(request,'TestApp/form_page.html',{'form':form})
