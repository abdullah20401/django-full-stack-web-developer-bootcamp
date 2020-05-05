from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'BasicApp/index.html')

def other(request):
    return render(request, 'BasicApp/other.html')

def relative(request):
    return render(request, 'BasicApp/relative_url_templates.html')