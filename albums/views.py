from django.shortcuts import render
from .models import Album
from .forms import AlbumForm

# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    # goes to the DataBase and gets all instznces of the
    # model Album (Django ORM) = query
    return render(request, 'albums/index.html', {'albums': albums})
    # pass data to the template using the context dictionary


def add_album(request):
    form = AlbumForm()
    return render(request, 'albums/add_album.html', {'form': form})
