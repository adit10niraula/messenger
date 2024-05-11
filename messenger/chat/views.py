from django.shortcuts import render
from .models import Friends,Profile,Message

# Create your views here.

def home(request):
    user = request.user.profile
    print(user)
    friends = user.friend.all()
    print(friends)


    context = {'friends':friends}
    return render(request, 'chat/home.html', context)




def detail(request):

    return render(request, 'chat/detail.html')