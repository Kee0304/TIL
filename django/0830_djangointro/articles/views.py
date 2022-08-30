from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dtl(request):
    name='KEE'
    context={
        'name':name,
        'age':29,
        'foods':['pasta','pizza','hamburger'],
    }
    return render(request, 'dtl.html', context)


def greeting(request):
    name="KEE"
    context={
        'name':name,
        'age':29,
        'foods':['pasta','pizza','hamburger'],
    }
    return render(request, 'greeting.html', context )

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    value = request.GET.get('search')
    name='KEE'
    context={
        'value':value,
        'name':name,
    }
    return render(request, 'catch.html', context)

def hello(request,name):
    context={
        'name' : name,
    }
    return render(request,'hello.html',context)