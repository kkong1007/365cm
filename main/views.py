from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request,'main/main.html')

def faq(request):
    return render(request,'main/faq.html')