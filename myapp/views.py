from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def gallery(request):
    return render(request,'gallery.html')
def form(request):
    return render(request,'form.html')
def table(request):
    return render(request,'table.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')