from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    daftar_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': daftar_katalog,
    'nama': 'Eldira Lahanny Permata Sherman'
    }
    return render(request, "katalog.html", context)
