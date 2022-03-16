from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,'Home/home.html')

def Rep(request):
    return render(request,'Class/msg.html')

