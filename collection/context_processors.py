from .models import Collection

def all_collections(request):
    collection_links = Collection.objects.all()
    return dict(collection_links=collection_links)