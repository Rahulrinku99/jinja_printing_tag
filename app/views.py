from django.shortcuts import render

# Create your views here.
def print_jinja(request):
    d={'name':'Rahul'}
    return render(request,'print_jinja.html',context=d)