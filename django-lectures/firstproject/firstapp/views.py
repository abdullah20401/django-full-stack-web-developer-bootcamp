from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_home': 'Hello, How are you!'}
    return render(request, 'firstapp/index.html', context=my_dict)

def bye(request):
    bye_content = {'insert_bye': "Bye, Hope to see you again!"}
    return render(request, 'firstapp/bye.html', context=bye_content)