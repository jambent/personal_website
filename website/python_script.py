from django.shortcuts import render

def button(request):

    return render(request,'detail.html')

def output(request):
    
    output_data = "A Python script has run"
    
    return render(request,"detail.html",{"output_data":output_data})
    