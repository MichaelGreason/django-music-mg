from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    form = AlbumForm()
    return render(request, 'albums/add_album.html', {'form': form})


def detail_album(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/detail_album.html', {'albums': albums})


def edit_album(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=albums)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    form = AlbumForm(instance=albums)
    return render(request, 'albums/edit_album.html', {'form': form, 'pk': pk})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('home')
    return render(request, 'albums/delete_album.html')
