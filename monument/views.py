from django.shortcuts import render, get_object_or_404
from .models import Monument

def home(request):
    monuments = Monument.objects.all()
    return render(request, 'monument/home.html', {'monuments': monuments})

def monument_detail(request, pk):
    monument = get_object_or_404(Monument, pk=pk)
    return render(request, 'monument/monument_detail.html', {'monument': monument})
