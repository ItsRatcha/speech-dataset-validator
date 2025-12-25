from django.shortcuts import render, get_object_or_404
from .models import Audio, Lang


# Create your views here.
def index(request):
    audios = Audio.objects.all()
    return render(request, 'index.html', {'audios': audios})


def langselect(request):
    langs = Lang.objects.all()
    return render(request, 'langselect.html', {'langs': langs})


def task(request, lang_id):
    lang = get_object_or_404(Lang, pk=lang_id)
    audios = Audio.objects.filter(lang=lang)
    return render(request, 'task.html', {'lang': lang, 'audios': audios})