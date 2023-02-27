from django.shortcuts import render
from .models import Album

# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    # goes to the DataBase and gets all instznces of the
    # model Album (Django ORM) = query
    return render(request, 'albums/index.html', {'albums': albums})
    # pass data to the template using the context dictionary
