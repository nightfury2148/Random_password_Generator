from django.shortcuts import render
from django.http import HttpResponse
from random import choices
# Create your views here.
def hello(request):
    return render(request,'get_pass/home.html')
def get_pass(request):
    all = list('')
    if request.GET.get('small'):
        all.extend("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('capital'):
        all.extend("ABCDEFGHIJKLMNOPQRSTVUWXYZ")
    if request.GET.get('numbers'):
        all.extend("1234567890")
    if request.GET.get("special"):
        all.extend("!@#$%^&*()~+/*-?><:][]")
    
    length = int(request.GET.get('Length','15'))
    all_pass = ''
    all_pass = choices(all,k=length)
    generated_passsowrd = "".join(all_pass)
    


    return render(request,'get_pass/get_pass.html', {'password':generated_passsowrd})
def aboutus(request):
    return render(request,'get_pass/aboutus.html')