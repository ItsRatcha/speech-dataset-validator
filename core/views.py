from django.shortcuts import render
from .models import Audio

# Create your views here.
def index(request):
    audios = Audio.objects.all()
    return render(request, 'index.html', {'audios': audios})