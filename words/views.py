from django.http import HttpResponse
from django.shortcuts import render

from . models import Word

# Create your views here.
def word_list(request):
    words = Word.objects.all()
    output = ', '.join([str(word) for word in words])
    return HttpResponse(output)
