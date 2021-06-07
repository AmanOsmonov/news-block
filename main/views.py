from django.shortcuts import render
from .models import News


def index(request):
        news=News.objects.all()
        return render(request,'main/index.html',{'news': news,})
def about(request):
        return render(request,'main/about.html')


# Create your views here.
