from django.shortcuts import render
from PyDictionary import PyDictionary


# Create your views here.

def index_view(request):
    return render(request,'Dictionary/index.html')


def word_view(request):
    search=request.GET.get('search')
    if request.GET.get('search').strip() == "":
        return render(request,'Dictionary/index.html')
    Dictionary = PyDictionary()
    meaning = Dictionary.meaning(search)
    
    context = {
        
        'meaning':meaning,
        

    }
    return render(request,'Dictionary/word.html',context)