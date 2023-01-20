from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from .models import Artwork
# from .forms import ArtworkForm

# Create your views here.
def artworks(request):
    # artworks = Artwork.objects.all()
    # context = {"artworks": artworks}
    # return render(request, "artworks/artworks.html", context)
    return render(request, "artworks/artworks.html")



# http://127.0.0.1:8000/artwork/1/
def artwork(request, pk):
    return render(request, "artworks/single-artwork.html")
    #  
    # artworkObj = Artwork.objects.get(id=pk)
    # tags = artworkObj.tags.all()
    # print("artworkObj:", artworkObj)
    # return render(
    #     request, "artworks/single-artwork.html", {"artwork": artworkObj, "tags": tags}
    # )