from django.shortcuts import render

# Create your views here.
def hai(request):
    d={'a':2,'b':5,'c':10}
    return render(request,'hai.html',context=d)