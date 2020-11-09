from django.shortcuts import render
from My_AppTwo.models import User

# Create your views here.
def index(request):
    return render(request, 'My_AppTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')

    user_dict =  {'users': user_list}
    return render(request, 'My_AppTwo/users.html', context=user_dict)
    