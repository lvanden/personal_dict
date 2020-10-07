from django.http import HttpResponse
from django.shortcuts import render

from .models import Word


def word_list(request):
    words = Word.objects.all()
    return render(request, 'words/word_list.html', {'words': words})