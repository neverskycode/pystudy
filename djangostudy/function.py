#from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse('hello')
    return render(request,'hello.html')
def count(request):
    #return HttpResponse('hello')
    #print(len(request.GET['jk']))
    total_count=len(request.GET['jk'])
    return render(request,'count.html',{'count':total_count})
