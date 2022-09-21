from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_mywatchlist_in_xml
from mywatchlist.views import show_mywatchlist_in_json 
from mywatchlist.views import show_film_json 
from mywatchlist.views import show_film_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_mywatchlist_in_xml, name='show_mywatchlist_in_xml'),
    path('json/', show_mywatchlist_in_json, name='show_mywatchlist_in_json'),
    path('json/<int:id>', show_film_json, name='show_film_json'), 
    path('xml/<int:id>', show_film_xml, name='show_film_xml'),
]