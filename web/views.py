from django.shortcuts import render
from django.http import HttpResponse
from collection.models import Collection

# Create your views here.

def index(request):
    collections = Collection.objects.all().filter(featured_collection = True)
    context = {
        'collections': collections
    }
    return render(request, "index.html", context)
