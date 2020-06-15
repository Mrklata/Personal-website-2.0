from django.shortcuts import render

from main.models import Language


def home_view(request):
    lang = Language.objects.all()
    return render(request, 'main/home.html', {"lang": lang})


def skill_view(request, title):
    lang = Language.objects.get(title__iexact=title)
    return render(request, 'main/skill.html', {"lang": lang})
